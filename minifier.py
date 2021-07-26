import json
from pathlib import Path
from typing import Iterable


def human_repr(num: float) -> str:
    for unit in ["B", "KB", "MB"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}"
        num = num / 1024.0
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
            f"\033[92m{before}\033[0m -> \033[92m{after}\033[0m. "
            f"Compressed: \033[92m{saved}\033[0m\n"
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
            f"\033[34m{rel_file}\033[0m : "
            "\033[92mminimized\033[0m : "
            f"\033[33m{before}\033[0m -> \033[92m{after}\033[0m"
        )
        print(info)


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "mimesis" / "data"
    files = sorted(data_dir.rglob("*.json"))
    Minimizer(files=files).run()
