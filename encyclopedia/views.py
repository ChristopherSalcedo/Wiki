from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from . import util
from django.urls import reverse 
from django.http import HttpResponseRedirect
from django import template
import random 
import difflib
from django import forms


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request,name):
    namedisplayed = util.get_entry(name.capitalize())
    if namedisplayed == None:
        return render(request,"encyclopedia/not_found.html")
    else:
        return render(request,"encyclopedia/entries.html",{
        "EntryContent": namedisplayed,
        "name":name.capitalize()
        })


def NewPage(request):
    if request.method == 'POST':
        pagename = str(request.POST.get("pagename"))
        pagecontent = str(request.POST.get("pagecontent"))
        if pagename and pagecontent:
            util.save_entry(pagename,pagecontent)
            return HttpResponseRedirect(reverse("encyclopedia:index"))
        else:
            return render(request, 'encyclopedia/NewPage.html',{
                "error":"<h5 style='color:red;'>Error you need write in all the text box area</h5>"
            })
    return render(request, 'encyclopedia/NewPage.html', {
    })

def search(request):
    if request.method == "GET":
        inputname = str(request.GET.get("q"))
        listname  = util.list_entries()
        if  inputname.capitalize() in listname or inputname in listname or inputname.upper() in listname or inputname.lower() in listname or inputname.title() in listname:
            return entries(request,inputname.capitalize())
        else:
            listname=[element.capitalize() for element in listname]
            listsearch = difflib.get_close_matches(inputname.capitalize(), listname,cutoff = 0.1)
            if listsearch:
                return render(request, 'encyclopedia/search.html', {
                "list_searched":listsearch
                })
            else:
                return render(request, 'encyclopedia/search.html', {
                "list_searched":[]
                })

def edit(request,value):
    content =  util.get_entry(value.capitalize())
    if request.method == 'POST':
        pagename = str(value.capitalize())
        pagecontent = str(request.POST.get("editcontent"))
        if pagecontent:
            util.save_entry(pagename,pagecontent)
            return HttpResponseRedirect(f"/wiki/{pagename}") 
        else:
            return render(request, 'encyclopedia/edit.html',{
                "error":"<h5 style='color:red;'>Error you need write in all the text box area</h5>"
            })
    else:
        return render(request,'encyclopedia/edit.html',{
        "name":value,
        "content":content
        })