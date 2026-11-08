
 Практична робота №5

Тема: Ініціалізація та конфігурація вебпроєктів з Django та Flask.

 Мета роботи

Навчитися створювати та налаштовувати вебпроєкти на Django та Flask, працювати з віртуальними середовищами, залежностями та маршрутизацією.

 Виконані завдання

1.1. Створення віртуального середовища та встановлення Django і Flask.

1.2. Відтворення середовища через requirements.txt.

2.1. Створення Django-проєкту та додатка pages.

2.2. Налаштування Django та перевірка безпеки.

3.1. Створення Flask-додатка з маршрутизацією та JSON API.

3.2. Порівняння файлових структур Django та Flask.

 Використані технології

Python 3.14.8

Django 6.1.3

Flask 3.1.3

HTML та CSS

 Встановлення

Створення віртуального середовища:

    python3 -m venv venv

Активація на macOS:

    source venv/bin/activate

Встановлення залежностей:

    python -m pip install -r requirements.txt

 Запуск Django

    cd mysite
    python manage.py runserver

Адреса: http://127.0.0.1:8000/

Доступні маршрути:

- /
- /about/
- /contact/
- /contact/?name=Nadia

 Запуск Flask

Із головної папки Practice_5:

    cd myflaskapp
    python app.py

Адреса: http://127.0.0.1:5000/

Доступні маршрути:

- /
- /about
- /api/info
- /greet/Nadia
- /greet?name=Student

Запуск програм перевірки

Із головної папки Practice_5:

    python practical_05_task_1_1.py
    python practical_05_task_1_2.py
    python practical_05_task_2_2.py
    python practical_05_task_3_2.py

 Порівняння проєктів

| Характеристика | Django | Flask |
|---|---:|---:|
| Python-файли | 14 | 2 |
| HTML-файли | 0 | 1 |
| CSS-файли | 0 | 1 |
| Каталоги | 3 | 2 |
| Розмір, байт | 6086 | 2771 |

 Висновок

Створено вебпроєкти на Django та Flask, налаштовано залежності, маршрутизацію та конфігурацію. Реалізовано вебсторінки, JSON API та перевірку безпеки. Проведено порівняння структури обох проєктів.
