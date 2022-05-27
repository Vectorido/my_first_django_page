from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverter, 'my_float')
register_converter(converters.MyDateConverter, 'my_date')

urlpatterns = [
    path('', views.index, name="main_index"),
    path('<yyyy:sign_zodiac>/', views.get_yyyy_converters, name='horoscope-name'),
    path('<my_date:sign_zodiac>/', views.get_mydate_converters),
    path('type/', views.get_info_list_of_types, name='horoscope-typelist'),
    path('type/<str:sign_type>', views.get_info_about_element, name='horoscope-types'),
    path('<int:sign_zodiac>/', views.get_info_about_sign_zodiac_by_number),
    path('<my_float:sign_zodiac>/', views.get_myfloat_converters),
    path('<str:sign_zodiac>/', views.get_info_about_sign_zodiac, name='horoscope-name'),
    path('<int:month>/<int:day>', views.get_info_by_date)
]



