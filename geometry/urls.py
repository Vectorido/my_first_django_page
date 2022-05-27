from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('rectangle/', views.rectangle_start, name='rectangle-start'),
    path('rectangle/<int:width>/<int:height>/', views.rectangle_area, name='rectangle-area'),
    path('square/<int:width>', views.square_area, name='square-area'),
    path('circle/<int:radius>', views.circle_area, name='circle-area'),
    path('get_rectangle_area/<int:width>/<int:height>', views.string_redirect),
    path('get_square_area/<int:width>', views.string_redirect),
    path('get_circle_area/<int:radius>', views.string_redirect),
]
