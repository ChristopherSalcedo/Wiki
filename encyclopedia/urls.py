from django.conf.urls import handler404
from django.urls import path
from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("search",views.search, name="search"),
    path("NewPage",views.NewPage, name="NewPage"),
    path("<str:name>",views.entries, name="entries"),
    path("<str:value>/edit",views.edit,name="edit")
]
