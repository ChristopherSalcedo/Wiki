from django.http import request
from django.http.response import HttpResponse
import markdown
from django import template
from django.template.defaultfilters import stringfilter
from .. import util,views
from django.urls import reverse
import random 
numurls=0

register = template.Library()

@register.filter(name="markdown")
def convert_markdown(value):
    return markdown.markdown(value)

@register.simple_tag(name="random_tag")
def random_url():
    list_of_route_names =  util.list_entries()
    name=random.choice(list_of_route_names)
    return name



