from django.urls import path, re_path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.title, name="title"),
    re_path(r"^wiki/(?P<title>).*[\s\w]*/$", views.wiki_entry, name="wiki_entry"),
    path("search", views.search, name="zoek"),
    path("add_file", views.add_file, name="add_file")
]
