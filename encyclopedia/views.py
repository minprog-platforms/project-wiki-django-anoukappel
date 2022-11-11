from django.shortcuts import render
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import markdown

class SaveNewPage(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label = "Content")

def convert_md_to_html(title):
    """
    converts markdown file ot html.
    """
    content = util.get_entry(title)
    if content == None:
        return None
    else:
        html = markdown(content)
        return html

def entry(request, title):
    html_content = convert_md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html", {
            "Error": "this entry is missing"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
        })


def search(request):
    """
    check of er iets in de search balk is gezocht. ('q')
        * als 'q' een entry is direct naar die pagina
        * anders show entries waar 'q' in voorkomt. als 'q'=py show
          list met python
    """
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_md_to_html(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": entry_search,
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


# Add a new Page
def add_file(request):
    return



    # match = []
    # return render(request, "encyclopedia/wiki.html", {
    #     # "content": util.get_entry(zoek),
    #     "query": query,
    #     "result": match
    #})


def title(request, title):
    """
    zorgt ervoor dat de content en de title van de pagina geprint kan worden in wiki/title
    """
    tekst = util.get_entry(title)
    if tekst:
        """
        als er tekst in de title.md file is convert markdown naar html en return
        html tekst en title, in .html file html|safe om juiste manier te displayen.
        """
        html = markdown(util.get_entry(title)).strip()
        return render(request, "encyclopedia/wiki.html", {
            "content": html,
            "title": title
        })
    else:
        return render(request, "encyclopedia/notfound.html", {
            "error": f"Error: Wiki page title '{title}' not found"
        })







def index(request):
    """
    Zorgt ervoor dat verschillende titles geprint kunnen worden op de hoofdpagina.
    """
    if request.GET.get('q'):
        search(request, request.GET['q'])
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
    })




def wiki_entry(request, title):
    """uitleg"""
    context = {}
    entry_list = utily.list_entries()

    #filter the title
    title = title.strip()
    wiki = [entry for entry in entry_list if title.lower() in entry.lower()]

    if not wiki or wiki is None:
        return redirect(notFound)

    # get Entry by its title
    entry = util.get_entry(wiki[0])
    content = markdown(entry).strip()
    return render(request, "encyclopedia/wiki.html", {
        "content": content,
        "title": title
    })
