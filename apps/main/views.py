from django.shortcuts import render, HttpResponse
from django.http.request import HttpRequest
from auths.models import Client

# Create your views here.
def simple(request: HttpRequest) -> HttpResponse:
    return HttpResponse(
        '<h1>Что нибудь</h1>'
    )


def index(request: HttpRequest) -> HttpRequest:
    """index view."""

    numbers: list[int] = []
    i: int
    for i in range(1, 11):
        numbers.append(i)

    ctx_data: dict[str, str | list[int]] = {
        'ctx_title': 'Заголовок главной страницы',
        'ctx_numbers': numbers
    }
    return render(
        request,
        template_name='main/index.html',
        context=ctx_data
    )

def get_all_users_view(request: HttpRequest):
    """users view"""

    print(Client.objects.all())
    return HttpResponse('ok')