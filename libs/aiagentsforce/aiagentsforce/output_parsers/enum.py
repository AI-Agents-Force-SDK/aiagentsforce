from enum import Enum
from typing import Dict, List, Type

from aiagentsforce_core.exceptions import OutputParserException
from aiagentsforce_core.output_parsers import BaseOutputParser
from aiagentsforce_core.utils import pre_init


class EnumOutputParser(BaseOutputParser[Enum]):
    """Parse an output that is one of a set of values."""

    enum: Type[Enum]
    """The enum to parse. Its values must be strings."""

    @pre_init
    def raise_deprecation(cls, values: Dict) -> Dict:
        enum = values["enum"]
        if not all(isinstance(e.value, str) for e in enum):
            raise ValueError("Enum values must be strings")
        return values

    @property
    def _valid_values(self) -> List[str]:
        return [e.value for e in self.enum]

    def parse(self, response: str) -> Enum:
        try:
            return self.enum(response.strip())
        except ValueError:
            raise OutputParserException(
                f"Response '{response}' is not one of the "
                f"expected values: {self._valid_values}"
            )

    def get_format_instructions(self) -> str:
        return f"Select one of the following options: {', '.join(self._valid_values)}"

    @property
    def OutputType(self) -> Type[Enum]:
        return self.enum
