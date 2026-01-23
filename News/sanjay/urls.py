from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("news/<str:category>/", views.news_list, name="news_list"),
]
