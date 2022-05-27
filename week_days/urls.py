from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="week"),
    path('<int:number>/', views.get_info_about_numbers),
    path('<sign_day>/', views.get_info_about_sign_days, name="week_days-name"),

]

