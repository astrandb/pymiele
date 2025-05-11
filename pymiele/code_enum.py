"""Classes for code enums."""

from enum import IntEnum
import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)
completed_warnings: set[str] = set()


class MieleEnum(IntEnum):
    """Miele Enum for codes with int values."""

    @property
    def name(self) -> str:
        """Force to lower case."""
        return super().name.lower()

    @classmethod
    def _missing_(cls, value: object) -> Any | None:
        if hasattr(cls, "unknown_code") or hasattr(cls, "unknown"):
            warning = (
                f"Missing {cls.__name__} code: {value} - defaulting to 'unknown_code'"
            )
            if warning not in completed_warnings:
                completed_warnings.add(warning)
                _LOGGER.warning(warning)
            return cls.unknown_code
        return None

    def __new__(cls, value: int, *values: list[int]) -> Any:
        """Allow duplicate values."""
        self = int.__new__(cls)
        self._value_ = value
        for v in values:
            self._add_value_alias_(v)
        return self

    @classmethod
    def as_dict(cls) -> dict[str, int]:
        """Return a dict of enum names and values."""
        return {i.name: i.value for i in cls if i.name != "unknown_code"}

    @classmethod
    def as_enum_dict(cls) -> dict[int, Any]:
        """Return a dict of enum values and enum names."""
        return {i.value: i for i in cls if i.name != "unknown_code"}

    @classmethod
    def values(cls) -> list[int]:
        """Return a list of enum values."""
        return list(cls.as_dict().values())

    @classmethod
    def keys(cls) -> list[str]:
        """Return a list of enum names."""
        return list(cls.as_dict().keys())

    @classmethod
    def items(cls) -> Any:
        """Return a list of enum items."""
        return cls.as_dict().items()
