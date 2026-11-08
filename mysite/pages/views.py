
from django.http import HttpResponse
from django.utils.html import escape


def index(request):
    # Головна сторінка
    return HttpResponse(
        "<h1>Головна сторінка Django</h1>"
        "<p>Практична робота №5</p>"
        "<ul><li>Маршрутизація</li>"
        "<li>Додатки</li>"
        "<li>Конфігурація</li></ul>"
    )


def about(request):
    # Інформація про проєкт
    return HttpResponse(
        "<h1>Про проєкт</h1>"
        "<p>Дисципліна: Програмування</p>"
        "<p>Практична робота №5</p>"
        "<p>Студент: Бублик Надія Олексіївна</p>"
    )


def contact(request):
    # Отримання імені з GET-запиту
    name = request.GET.get("name", "").strip()

    if name:
        return HttpResponse(f"<h1>Вітаємо, {escape(name)}!</h1>")

    return HttpResponse("<h1>Контактна сторінка</h1>")
