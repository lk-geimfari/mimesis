from pathlib import Path
from typing import Final

__all__ = ["DATADIR", "LOCALE_SEP"]

# This is the path to the data directory in the mimesis package.
DATADIR: Final[Path] = Path(__file__).parent / "datasets"

LOCALE_SEP: Final[str] = "-"
