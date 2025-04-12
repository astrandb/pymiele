"""Library for Miele API."""

from __future__ import annotations

from abc import ABC, abstractmethod
import asyncio
from collections.abc import Callable, Coroutine
import json
from json.decoder import JSONDecodeError
import logging
from typing import Any

from aiohttp import ClientResponse, ClientResponseError, ClientSession, ClientTimeout

from .const import AIO_TIMEOUT, MIELE_API, VERSION

CONTENT_TYPE = "application/json"
USER_AGENT_BASE = f"Pymiele/{VERSION}"

_LOGGER = logging.getLogger(__name__)


class AbstractAuth(ABC):
    """Abstract class to make authenticated requests."""

    def __init__(self, websession: ClientSession, host: str) -> None:
        """Initialize the auth."""
        self.websession = websession
        self.host = host

    @abstractmethod
    async def async_get_access_token(self) -> str:
        """Return a valid access token."""

    async def request(self, method: str, url: str, **kwargs: Any) -> ClientResponse:
        """Make a request."""
        if headers := kwargs.pop("headers", {}):
            headers = dict(headers)

        agent_suffix = kwargs.pop("agent_suffix", None)
        user_agent = (
            USER_AGENT_BASE
            if agent_suffix is None
            else f"{USER_AGENT_BASE}; {agent_suffix}"
        )

        access_token = await self.async_get_access_token()
        headers["Authorization"] = f"Bearer {access_token}"
        headers["User-Agent"] = user_agent

        # _LOGGER.debug("Request headers: %s", headers)

        return await self.websession.request(
            method,
            f"{self.host}{url}",
            **kwargs,
            headers=headers,
        )

    async def get_devices(self) -> dict:
        """Get all devices."""
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "GET", "/devices", headers={"Accept": "application/json"}
            )
            res.raise_for_status()
        return await res.json()

    async def get_actions(self, serial: str) -> dict:
        """Get actions for a device."""
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "GET",
                f"/devices/{serial}/actions",
                headers={"Accept": "application/json"},
            )
            res.raise_for_status()
        return await res.json()

    async def get_programs(self, serial: str) -> dict:
        """Get programs for a device."""
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "GET",
                f"/devices/{serial}/programs",
                headers={"Accept": "application/json"},
            )
            res.raise_for_status()
        return await res.json()

    async def get_rooms(self, serial: str) -> dict:
        """Get rooms for a device."""
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "GET",
                f"/devices/{serial}/rooms",
                headers={"Accept": "application/json"},
            )
            res.raise_for_status()
        return await res.json()

    async def set_target_temperature(
        self, serial: str, temperature: float, zone: int = 1
    ) -> ClientResponse:
        """Set target temperature."""
        temp = round(temperature)
        async with asyncio.timeout(AIO_TIMEOUT):
            data = {"targetTemperature": [{"zone": zone, "value": temp}]}
            res = await self.request(
                "PUT",
                f"/devices/{serial}/actions",
                data=json.dumps(data),
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Accept": "application/json",
                },
            )
            res.raise_for_status()
        _LOGGER.debug("set_target res: %s", res.status)
        return res

    async def send_action(
        self, serial: str, data: dict[str, str | int | bool]
    ) -> ClientResponse:
        """Send action command."""

        _LOGGER.debug("send_action serial: %s, data: %s", serial, data)
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "PUT",
                f"/devices/{serial}/actions",
                data=json.dumps(data),
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Accept": "application/json",
                },
            )
            res.raise_for_status()
        _LOGGER.debug("send_action res: %s", res.status)
        return res

    async def set_program(
        self, serial: str, data: dict[str, int | list[int]]
    ) -> ClientResponse:
        """Send start program command."""

        _LOGGER.debug("set_program serial: %s, data: %s", serial, data)
        async with asyncio.timeout(AIO_TIMEOUT):
            res = await self.request(
                "PUT",
                f"/devices/{serial}/programs",
                data=json.dumps(data),
                headers={
                    "Content-Type": CONTENT_TYPE,
                    "Accept": "application/json",
                },
            )
            res.raise_for_status()
        _LOGGER.debug("set_program res: %s", res.status)
        return res

    async def listen_events(
        self,
        data_callback: Callable[[dict[str, Any]], Any] | None = None,
        actions_callback: Callable[[dict[str, Any]], Any] | None = None,
    ) -> Callable[[], Coroutine[Any, Any, None]]:
        """Listen to events, apply changes to object and call callback with event."""
        while True:
            try:
                access_token = await self.async_get_access_token()
                async with self.websession.get(
                    f"{MIELE_API}/devices/all/events",
                    timeout=ClientTimeout(total=None, sock_connect=5, sock_read=None),
                    headers={
                        "Accept": "text/event-stream; char-set=utf-8",
                        "Authorization": f"Bearer {access_token}",
                    },
                ) as resp:
                    # _LOGGER.debug("Starting listening for events: %s", resp.status)
                    while True:
                        # add 120s timeout for reading event data, ping is every 20s
                        # if ping is not received, then connection must be closed and re-initialized
                        try:
                            id_line = await asyncio.wait_for(
                                resp.content.readline(), timeout=120
                            )
                        except asyncio.exceptions.TimeoutError:
                            resp.close()
                            _LOGGER.warning(
                                "Ping timeout, closing connection and restarting"
                            )
                            break
                        data_line = await resp.content.readline()
                        await resp.content.readline()  # Empty line
                        if resp.closed:
                            _LOGGER.warning("Connection was closed, restarting")
                            break
                        event_type = bytearray(id_line).decode().strip()
                        if event_type == "event: devices":
                            data = json.loads(data_line[6:])
                            if data_callback is not None:
                                asyncio.create_task(data_callback(data))  # noqa: RUF006
                        elif event_type == "event: actions":
                            data = json.loads(data_line[6:])
                            if actions_callback is not None:
                                asyncio.create_task(actions_callback(data))  # noqa: RUF006
                        elif event_type == "event: ping":
                            # _LOGGER.debug("Ping SSE")
                            pass
                        else:
                            _LOGGER.error("Unknown event type: %s", event_type)

            except ClientResponseError as ex:
                _LOGGER.error("SSE: %s - %s", ex.status, ex.message)
                await asyncio.sleep(5)
            except JSONDecodeError as ex:
                _LOGGER.error(
                    "JSON decode error: %s, Pos: %s, Doc: %s", ex.msg, ex.pos, ex.doc
                )
                await asyncio.sleep(5)
            except Exception as ex:  # pylint: disable=broad-except
                _LOGGER.error("Listen_event: %s", ex)
                await asyncio.sleep(5)


class MieleException(Exception):
    """Generic miele exception."""


class MieleAuthException(MieleException):
    """Authentication failure."""
