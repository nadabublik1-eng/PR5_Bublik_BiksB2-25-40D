
from pathlib import Path


IGNORED_DIRS = {"venv", "venv2", ".venv", "__pycache__", ".git"}
IGNORED_FILES = {"db.sqlite3", ".DS_Store"}


def visible_entries(path: Path) -> list[Path]:
    return sorted(
        (
            item for item in path.iterdir()
            if item.name not in IGNORED_DIRS | IGNORED_FILES
            and item.suffix != ".pyc"
        ),
        key=lambda item: (not item.is_dir(), item.name.lower())
    )


def scan_directory(path: str, prefix: str = "") -> list[str]:
    # Рекурсивне формування дерева файлів
    tree = []
    entries = visible_entries(Path(path))

    for index, entry in enumerate(entries):
        last = index == len(entries) - 1
        branch = "└── " if last else "├── "
        tree.append(prefix + branch + entry.name + ("/" if entry.is_dir() else ""))

        if entry.is_dir():
            next_prefix = prefix + ("    " if last else "│   ")
            tree.extend(scan_directory(str(entry), next_prefix))

    return tree


def analyze_project(path: str) -> dict:
    # Підрахунок файлів, каталогів та розміру
    root = Path(path)
    stats = {
        "py_files": 0,
        "html_files": 0,
        "css_files": 0,
        "total_size": 0,
        "directories": []
    }

    def visit(folder: Path):
        for entry in visible_entries(folder):
            if entry.is_dir():
                stats["directories"].append(str(entry.relative_to(root)))
                visit(entry)
            elif entry.is_file():
                if entry.suffix == ".py":
                    stats["py_files"] += 1
                elif entry.suffix == ".html":
                    stats["html_files"] += 1
                elif entry.suffix == ".css":
                    stats["css_files"] += 1

                stats["total_size"] += entry.stat().st_size

    visit(root)
    return stats


def compare_projects(django_path: str, flask_path: str):
    for name, path in [("Django", django_path), ("Flask", flask_path)]:
        print(f"\n{name}:")
        for line in scan_directory(path):
            print(line)

    django = analyze_project(django_path)
    flask = analyze_project(flask_path)

    print("\nПорівняльна таблиця")
    print(f"{'Характеристика':<22} {'Django':>10} {'Flask':>10}")

    rows = [
        ("Файли .py", "py_files"),
        ("Файли .html", "html_files"),
        ("Файли .css", "css_files"),
        ("Каталоги", "directories"),
        ("Розмір, байт", "total_size")
    ]

    for label, key in rows:
        d = len(django[key]) if key == "directories" else django[key]
        f = len(flask[key]) if key == "directories" else flask[key]
        print(f"{label:<22} {d:>10} {f:>10}")


def main():
    root = Path(__file__).resolve().parent
    django_path = root / "mysite"
    flask_path = root / "myflaskapp"

    if not django_path.is_dir() or not flask_path.is_dir():
        print("Не знайдено папку mysite або myflaskapp")
        return

    compare_projects(str(django_path), str(flask_path))


if __name__ == "__main__":
    main()
