from django.urls import path

from . import views

# app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.wiki, name="title"),
    path("search/", views.search, name="zoek"),
    path("new_page/", views.new_page, name="new_page")
]
