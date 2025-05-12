"""Enum class for Miele intergration."""

from enum import IntEnum
import logging
from typing import Any

_LOGGER = logging.getLogger(__name__)
completed_warnings: set[str] = set()


class MieleEnum(IntEnum):
    """Miele Enum for codes with int values."""

    # Modify the behaviour of the class when detecting a missing value:
    # Add a member missing2none in order to:
    # - Log a warning that the code is missing
    # - Return None as key name
    #
    # Add a member unknown_code in order to:
    # - Log a warning that the code is missing
    # - Return 'unknown_value' as key name

    @property
    def name(self) -> str | None:
        """Force to lower case."""
        _name = super().name.lower()
        return _name if _name != "missing2none" else None

    @classmethod
    def _missing_(cls, value: object) -> Any | None:
        if hasattr(cls, "unknown_code") or hasattr(cls, "unknown"):
            warning = (
                f"Missing {cls.__name__} code: {value} - defaulting to 'unknown_code'"
            )
            if warning not in completed_warnings:
                completed_warnings.add(warning)
                _LOGGER.warning(warning)
            return cls.unknown_code  # pylint: disable=no-member
        if hasattr(cls, "missing2none"):
            warning = f"Missing {cls.__name__} code: {value} - defaulting to Unknown"
            if warning not in completed_warnings:
                completed_warnings.add(warning)
                _LOGGER.warning(warning)
            return cls.missing2none  # pylint: disable=no-member

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
        return {i.name: i.value for i in cls if i.name is not None}

    @classmethod
    def as_enum_dict(cls) -> dict[int, Any]:
        """Return a dict of enum values and enum names."""
        return {i.value: i for i in cls if i.name is not None}

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
