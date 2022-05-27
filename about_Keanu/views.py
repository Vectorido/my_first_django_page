from django.shortcuts import render
from django.urls import reverse


# Create your views here.

# def null_index(request):
#     zodiacs = list(zodiac_dict)
#     context = {
#         'zodiacs': zodiacs,
#         'zodiac_dict': zodiac_dict
#     }
#     return render(request, 'horoscope/index.html', context=context)

def index(request):
    reeves_info = {
        'year_born': '1964',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }

    return render(request, 'about_Keanu/main_page.html', context=reeves_info)



