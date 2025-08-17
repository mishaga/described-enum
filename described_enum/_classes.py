import enum


class DescribedEnum(enum.Enum):

    def __new__(cls, value: object, description: str | None = None) -> object:
        obj = object.__new__(cls)
        obj._value_ = value
        obj._description_ = description
        return obj

    @enum.property
    def description(self) -> str:
        """Description for the member."""
        return self._description_


class DescribedStrEnum(enum.StrEnum):

    def __new__(cls, value: str, description: str | None = None) -> str:
        if not isinstance(value, str):
            raise TypeError(f'Value must be of type str, got {type(value).__name__} {value!r}')

        obj = str.__new__(cls, value)
        obj._value_ = value
        obj._description_ = description
        return obj

    @enum.property
    def description(self) -> str:
        """Description for the member."""
        return self._description_


class DescribedIntEnum(enum.IntEnum):

    def __new__(cls, value: int, description: str | None = None) -> int:
        if not isinstance(value, int):
            raise TypeError(f'Value must be of type int, got {type(value).__name__} {value!r}')

        obj = int.__new__(cls, value)
        obj._value_ = value
        obj._description_ = description
        return obj

    @enum.property
    def description(self) -> str:
        """Description for the member."""
        return self._description_
