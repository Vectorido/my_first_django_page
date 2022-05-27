from django.shortcuts import render
from math import pi
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, 'geometry/index_calc.html')


def rectangle_start(request):
    return render(request, 'geometry/rectangle.html')


def string_redirect(request, width=None, height=None, radius=None):
    match [width, height, radius]:
        case [None, None, radius]:
            redirect_url = reverse('circle-area', args=(radius,))
            return HttpResponseRedirect(redirect_url)
        case [width, None, None]:
            redirect_url = reverse('square-area', args=(width,))
            return HttpResponseRedirect(redirect_url)
        case [width, height, None]:
            redirect_url = reverse('rectangle-area', args=(width, height))
            return HttpResponseRedirect(redirect_url)
        case _:
            return HttpResponseNotFound("Ошибка")


def rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата со стороной {width} равна {width ** 2}')


def circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга с радиусом {radius} с округлением до сотых равна {round(pi * radius ** 2, 2)}')
