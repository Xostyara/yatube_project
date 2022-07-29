from re import template
from django.shortcuts import render, HttpResponse

# Create your views here.
# Главная страница
def index(request): 
    template = 'posts/index.html'   
    return render(request, template)


# Страница с постами группы
def group_posts(request, slug):
    template = 'posts/group_list.html'
    return render(request, template, slug)


