
import ast
from pathlib import Path


def read_assignments(settings_path: str) -> dict:
    # Зчитування налаштувань без виконання файлу
    source = Path(settings_path).read_text(encoding="utf-8")
    tree = ast.parse(source)
    variables = {}

    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables[target.id] = node.value

    return variables


def analyze_settings(settings_path: str) -> dict:
    # Отримання основних параметрів Django
    variables = read_assignments(settings_path)
    config = {}

    for name in ["DEBUG", "INSTALLED_APPS", "LANGUAGE_CODE", "TIME_ZONE"]:
        node = variables.get(name)

        if node is not None:
            try:
                config[name] = ast.literal_eval(node)
            except (ValueError, TypeError):
                config[name] = ast.unparse(node)

    databases = variables.get("DATABASES")
    engine = "Не визначено"

    if isinstance(databases, ast.Dict):
        for key, value in zip(databases.keys, databases.values):
            if isinstance(key, ast.Constant) and key.value == "default":
                if isinstance(value, ast.Dict):
                    for inner_key, inner_value in zip(value.keys, value.values):
                        if isinstance(inner_key, ast.Constant) and inner_key.value == "ENGINE":
                            engine = ast.literal_eval(inner_value)

    config["DATABASES"] = engine
    return config


def check_security(settings_path: str) -> list[str]:
    # Перевірка трьох правил безпеки
    variables = read_assignments(settings_path)
    warnings = []

    debug = ast.literal_eval(variables["DEBUG"])
    hosts = ast.literal_eval(variables["ALLOWED_HOSTS"])
    secret = ast.unparse(variables["SECRET_KEY"])

    if debug:
        warnings.append("DEBUG=True небезпечний для production")

    if "os.environ" not in secret and "os.getenv" not in secret:
        warnings.append("SECRET_KEY записаний безпосередньо в коді")
    elif "dev-only" in secret:
        warnings.append("SECRET_KEY містить тестове значення")

    if not hosts:
        warnings.append("ALLOWED_HOSTS порожній")

    return warnings


def main():
    settings_path = Path(__file__).parent / "mysite" / "mysite" / "settings.py"

    if not settings_path.exists():
        print("Файл settings.py не знайдено")
        return

    config = analyze_settings(str(settings_path))

    print("Конфігурація Django:")
    for name, value in config.items():
        print(f"{name}: {value}")

    print("Перевірка безпеки:")
    warnings = check_security(str(settings_path))

    if warnings:
        for warning in warnings:
            print(warning)
    else:
        print("Попереджень не знайдено")


if __name__ == "__main__":
    main()
