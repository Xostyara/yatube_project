from django.shortcuts import render, HttpResponse

# Create your views here.
# Главная страница
def index(request):    
    return HttpResponse('Всем привет! Это Главная страница')


# Страница с постами группы
def group_posts(request, slug):
    return HttpResponse(f'Это страница groups {slug}')


