
import json
import subprocess
import sys
from pathlib import Path


def get_installed_packages() -> list[dict]:
    # Отримання пакетів через pip у форматі JSON
    result = subprocess.run(
        [sys.executable, "-m", "pip", "list", "--format=json"],
        capture_output=True,
        text=True,
        check=True
    )
    return json.loads(result.stdout)


def generate_requirements(
    packages: list[dict],
    filename: str = "requirements.txt"
) -> None:
    excluded = {"pip", "setuptools", "wheel"}

    lines = [
        f'{item["name"]}=={item["version"]}'
        for item in sorted(packages, key=lambda item: item["name"].lower())
        if item["name"].lower() not in excluded
    ]

    Path(filename).write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8"
    )


def verify_requirements(filename: str = "requirements.txt") -> bool:
    path = Path(filename)

    if not path.is_file():
        print("Файл requirements.txt не знайдено")
        return False

    installed = {
        item["name"].lower().replace("_", "-"): item["version"]
        for item in get_installed_packages()
    }

    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        name, separator, version = line.partition("==")

        if not separator or installed.get(name.lower().replace("_", "-")) != version:
            print("Не збігається:", line)
            return False

    return True


def main() -> None:
    packages = get_installed_packages()

    print("Знайдено пакетів:", len(packages))

    for item in packages[:10]:
        print(f'{item["name"]}=={item["version"]}')

    generate_requirements(packages)
    print("requirements.txt створено")
    print("Перевірка залежностей:", verify_requirements())


if __name__ == "__main__":
    main()
