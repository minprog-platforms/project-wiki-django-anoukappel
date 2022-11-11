from django.shortcuts import render
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import markdown
from random import randint


def index(request):
    """
    Zorgt ervoor dat verschillende titles geprint kunnen worden op de homepagina.
    """
    if request.GET.get('q'):
        search(request, request.GET['q'])
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
    })

def convert_md_to_html(title):
    """
    converts markdown file ot html of given title.
    use get_entry to get content of file.
    If succes return true else false.
    """
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        html = markdown(content)
        return html


def entry(request, title):
    """
    Geeft titel en content in html door naar wiki.html zodat dit weergegeven kan worden.
    """
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "Error": "this entry is missing"
        })
    else:
        return render(request, "encyclopedia/wiki.html", {
            "content": html_content,
            "title": title
        })


def search(request):
    """
    check of er iets in de search balk is gezocht. ('zoekterm')
        * als 'zoekterm' een entry is direct naar die pagina
        * anders show entries waar 'zoekterm' in voorkomt. als 'zoekterm'=py show
          list met python.
    """
    if request.method == "POST":
        entry_search = request.POST['zoekterm']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/wiki.html", {
                "content": html_content
            })
        else:
            allEntries = util.list_entries()
            recommendation = []
            for entry in allEntries:
                if entry_search.lower() in entry.lower():
                    recommendation.append(entry)
            return render(request, "encyclopedia/search.html", {
                "recommendation": recommendation
            })


def new_page(request):
    """
    wanneer op new_page gedrukt wordt (GET), naar pagina waar title en content ingevuld kan worden.
    Wanneer POST method (op button), check of title al bestaat en render  error page
    anders save as new file en render naar wiki.html met nieuwe titel en content.
    """
    if request.method == "GET":
        return render(request, "encyclopedia/new_page.html")
    else:
        title = request.POST['title']
        content = request.POST['Content']
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": "Entry page already exists"
            })
        else:
            util.save_entry(title, content)
            html_content = convert_md_to_html(title)
            return render(request, "encyclopedia/wiki.html", {
                "title": title,
                "content": html_content
            })

def random_page(request):
    """
    render wiki.html van een random title.
    """
    length_list = len(util.list_entries())
    list = util.list_entries()
    content = convert_md_to_html(list[randint(0, length_list - 1)])
    title = list[randint(0, length_list - 1)]
    return render(request, "encyclopedia/wiki.html", {
        "content": content,
        "title": title
    })

def change_page(request):
    """
    wanneer POST method (wiki.html) render change_page.
    waar je title en content van pagina kunt aanpassen.
    """
    if request.method == "POST":
        title = request.POST['entry_title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/change_page.html", {
            "content": content,
            "title": title
        })

def save_edit_page(request):
    """
    sla aangepaste pagina op.
    """
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['Content']
        util.save_entry(title, content)
        html_content = convert_md_to_html(title)
        return render(request, "encyclopedia/wiki.html", {
            "title": title,
            "content": html_content
        })
