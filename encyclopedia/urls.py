from django.urls import path, re_path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("new_page/", views.new_page, name="new_page"),
    path("random_page/", views.random_page, name="random_page"),
    path("change_page/", views.change_page, name="change_page"),
    path("save_edit_page/", views.save_edit_page, name="save_edit_page")
]
