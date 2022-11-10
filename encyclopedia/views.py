from django.shortcuts import render
from . import util
from django import forms
# from markdown2 import Markdown

# creating a form
class InputForm(forms.Form):
    title = forms.CharField(max_length = 200)
    content = forms.CharField()


def index(request):
    """
    Zorgt ervoor dat verschillende titles geprint kunnen worden op de hoofdpagina.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def wiki(request, title):
    """
    zorgt ervoor dat de content en de title van de pagina geprint kan worden in wiki.html.
    """
    return render(request, "encyclopedia/wiki.html", {
        "content": util.get_entry(title),
        "title": title
    })

def search(request, zoek):
    """
    zorgt ervoor dat de content en de title van de pagina geprint kan worden in wiki.html.
    """
    return render(request, "encyclopedia/wiki.html", {
        "content": util.get_entry(zoek),
        "title": zoek
    })

# def search(request):
#     return render(request, "encyclopedia/layout.html", {
#
#     })


def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
    "title": "Title",
    "edit": False,
    "editpage":InputForm()
    })
    # context ={}
    # context['form'] = InputForm()
    # return render(request, "encyclopedia/new_page.html", context)


# def entry_page(request):
#     return render(request, "encyclopedia/entry_page.html",{
#         "title": util.get_entry(index)
#     })
