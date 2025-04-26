import json
from pathlib import Path
from typing import Iterable

from colorama import Fore, Style

MIMESIS_DIR = Path(__file__).parent.parent.joinpath("mimesis")


def human_repr(num: float) -> str:
    for unit in ["B", "KB", "MB"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}"
        num /= 1024.0
    return f"{num:.1f}"


class Minimizer:
    """Minify content of all json files for all locales."""

    def __init__(self, *, files: Iterable[Path]) -> None:
        """Find all files of all locales."""
        self.files = files
        self.before_total = 0
        self.after_total = 0

    def run(self) -> None:
        """Start json minimizer and exit when all json files were minimized."""
        for file in self.files:
            self.minify(file)

        after = human_repr(self.after_total)
        before = human_repr(self.before_total)
        saved = human_repr(self.before_total - self.after_total)

        info = (
            "\nTotal: "
            f"{Fore.LIGHTGREEN_EX}{before}{Style.RESET_ALL} -> {Fore.LIGHTGREEN_EX}{after}{Style.RESET_ALL}. "
            f"Compressed: {Fore.LIGHTGREEN_EX}{saved}{Style.RESET_ALL}\n"
        )
        print(info)

    def minify(self, file: Path) -> None:
        size_before = file.stat().st_size
        self.before_total += size_before
        before = human_repr(size_before)

        minimized = json.dumps(
            json.loads(file.read_text()), separators=(",", ":"), ensure_ascii=False
        )
        file.write_text(minimized)

        size_after = file.stat().st_size
        self.after_total += size_after
        after = human_repr(size_after)

        rel_file = file.relative_to(file.parent.parent)
        info = (
            f"{Fore.BLUE}{str(rel_file):<30}{Style.RESET_ALL} : "
            f"{Fore.LIGHTGREEN_EX}minimized{Style.RESET_ALL} : "
            f"{Fore.YELLOW}{before:<7}{Style.RESET_ALL} -> {Fore.LIGHTGREEN_EX}{after:<7}{Style.RESET_ALL}"
        )
        print(info)


if __name__ == "__main__":  # pragma: no cover
    data_dir = MIMESIS_DIR / "datasets"
    files = sorted(data_dir.rglob("*.json"))
    Minimizer(files=files).run()
