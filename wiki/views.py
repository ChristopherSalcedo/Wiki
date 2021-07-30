from django.shortcuts import redirect, render
def page_not_found(request,exception):
    return render(request,"encyclopedia/not_found.html")