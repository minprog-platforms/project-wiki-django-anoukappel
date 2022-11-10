from django.shortcuts import render
from . import util
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
from markdown2 import markdown

class SaveNewPage(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label = "Content")


# Add a new Page
def add_file(request):
    return render(request, "encyclopedia/add_file.html", {
        "form": SaveNewPage()
    })
#
# # add a new Page
# def add_file(request):
#     #check if method is POST
#     if request.method == "POST":
#
#     # Take in the data the user submitted and save it as form
#         title = SaveNewPage(request.POST)
#
#     # check if form data is valid server_side
#     if form.is_valid():
#
#         #isolate the task from the 'cleaned' version of the form data
#         file = title.cleaned_data["task"]
#
#         # Add the new task to out
#         tasks.append(task)
#
#         # redirect user to list of tasks
#         return HttpResponseRedirect(reverse("encyclopedia/add_file.html"))
#     else:
#         # If the form invalid, re-render the page with existing information.
#         return render(request, "encyclopedia/add_file.html", {
#                  "form": form
#         })
#          return render(request, "encyclopedia/add_file.html", {
#         "form": SaveNewPage
#     })


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

def search(request, query):
    """
    z
    """
    match = []
    return render(request, "encyclopedia/wiki.html", {
        # "content": util.get_entry(zoek),
        "query": query,
        "result": match
    })

def title(request, title):
    """
    zorgt ervoor dat de content en de title van de pagina geprint kan worden in wiki.html.
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
