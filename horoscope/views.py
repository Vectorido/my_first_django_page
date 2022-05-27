from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from datetime import datetime, date

# Create your views here.

zodiac_dict = {
    'aries': '♈ Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': '♉ Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': '♊ Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': '♋ Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': '♌ Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': '♍ Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': '♎ Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': '♏ Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': '♐ Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': '♑ Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': '♒ Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': '♓ Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}

types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}

dict_date = {"aries": [date(2000, 3, 21), date(2000, 4, 20)],
             "taurus": [date(2000, 4, 21), date(2000, 5, 21)],
             "gemini": [date(2000, 5, 22), date(2000, 6, 21)],
             "cancer": [date(2000, 6, 22), date(2000, 7, 22)],
             "leo": [date(2000, 7, 23), date(2000, 8, 21)],
             "virgo": [date(2000, 8, 22), date(2000, 9, 23)],
             "libra": [date(2000, 9, 24), date(2000, 10, 23)],
             "scorpio": [date(2000, 10, 24), date(2000, 11, 22)],
             "sagittarius": [date(2000, 11, 23), date(2000, 12, 22)],
             "capricorn": [date(2000, 12, 23), date(2000, 1, 20)],
             "aquarius": [date(2000, 1, 21), date(2000, 2, 19)],
             "pisces": [date(2000, 2, 20), date(2000, 3, 20)]
             }


def get_mydate_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали дату - {sign_zodiac}')


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали число из четырех цифр - {sign_zodiac}')


def get_myfloat_converters(request, sign_zodiac):
    return HttpResponse(f'Вы передали вещественное число - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        'zodiacs': zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context=context)


def get_info_list_of_types(request):
    t_elements = ''
    for _ in types:
        redirect_path = reverse("horoscope-types", args=[_])
        t_elements += f"<li> <a href='{redirect_path}'> {_.title()} </a> </li>"
    response = f"<ul>{t_elements}</ul>"
    return HttpResponse(response)


def get_info_about_element(request, sign_type: str):
    if sign_type not in ('fire', 'air', 'water', 'earth'):
        return HttpResponseNotFound(f"Некорректно задана стихия")
    zod_elements = ''
    for zod_el in types[sign_type]:
        redirect_path = reverse("horoscope-name", args=[zod_el])
        zod_elements += f"<li> <a href='{redirect_path}'> {zod_el.title()} </a> </li>"
    return HttpResponse(zod_elements)


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    zodiacs = list(zodiac_dict)
    description = zodiac_dict.get(sign_zodiac, None)
    data = {
        'description_zodiac': description,
        'title_zodiac': sign_zodiac,
        'zodiacs': zodiacs,
        'sign_name': description.split()[1],
    }
    return render(request, 'horoscope/info_zodiac.html', context=data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponse(f'Неправильный номер знака зодиака - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=[name_zodiac])
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month, day):
    try:
        req_date = date(2000, month, day)
        for k, v in dict_date.items():
            if v[0] <= req_date <= v[1]:
                redirect_url = reverse("horoscope-name", args=[k])
                return HttpResponseRedirect(redirect_url)
        return HttpResponseRedirect(reverse("horoscope-name", args=['capricorn']))
    except ValueError:
        return HttpResponseNotFound(f'<h2>ОШИБКА</h2><br> Месяц и день должны быть в пределах своего диапазона')

# old_code

# def get_info_about_sign_zodiac(request, sign_zodiac: str):
#     description = zodiac_dict.get(sign_zodiac, None)
#     if description:
#         return HttpResponse(f'<h2>{description}</h2>')
#     else:
#         return HttpResponseNotFound(f"Неизвестный знак зодиака - {sign_zodiac}")

#     zodiacs = list(zodiac_dict)
#     li_elements = ''
#     for sign in zodiacs:
#         redirect_path = reverse("horoscope-name", args=[sign])
#         li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
#     response = f"<ul>{li_elements}</ul>"
#     redirect_for_type = reverse("horoscope-typelist")
#     response += f"<li> <a href='{redirect_for_type}'> TYPES </a> </li>"
# {% url 'main_index' %}
#
#
# @dataclass
# class Person:
#     name: str
#     age: int
#
#     def __str__(self):
#         return f"This is {self.name}, his age is {self.age}"
