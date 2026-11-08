
import importlib
import importlib.metadata
import sys


def check_python_version() -> bool:
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    supported = version >= (3, 10)
    print("Підтримується:", supported)
    return supported


def check_package(package_name: str) -> bool:
    # Перевірка встановлення та версії пакета
    try:
        importlib.import_module(package_name)
        version = importlib.metadata.version(package_name)
    except (ImportError, importlib.metadata.PackageNotFoundError):
        print(f"{package_name}: не встановлено")
        return False

    print(f"{package_name}: {version}")
    return True


def main() -> None:
    check_python_version()
    packages = ["django", "flask"]
    installed = {name: check_package(name) for name in packages}

    print("Встановлено:", sum(installed.values()))
    print("Відсутні:", len(packages) - sum(installed.values()))

    missing = [name for name, exists in installed.items() if not exists]
    if missing:
        print("Команда встановлення: python -m pip install " + " ".join(missing))


if __name__ == "__main__":
    main()
