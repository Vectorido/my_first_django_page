from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

days_dict = {'monday': '<strong>To-do list for Monday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'tuesday': '<strong>To-do list for Tuesday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'wednesday': '<strong>To-do list for Wednesday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'thursday': '<strong>To-do list for Thursday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'friday': '<strong>To-do list for Friday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'saturday': '<strong>To-do list for Saturday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             'sunday': '<strong>To-do list for Sunday:</strong><br><br>1. Work hard<br>2. Be good<br>3. Buy some stuff',
             }


def index(request):
    return render(request, 'week_days/greeting.html')


def get_info_about_sign_days(request, sign_day):
    description_d = days_dict.get(sign_day, None)
    if description_d:
        return HttpResponse(description_d)
    else:
        return HttpResponseNotFound(f"Unknown day of the week - {sign_day}")


# old_code

def get_info_about_numbers(request, number: int):
    days_list = list(days_dict)
    if number > len(days_list) or number == 0:
        return HttpResponseNotFound(f"Incorrect day's number of the week - {number}")
    day = days_list[number - 1]
    redirect_url = reverse("week_days-name", args=[day])
    return HttpResponseRedirect(redirect_url)
