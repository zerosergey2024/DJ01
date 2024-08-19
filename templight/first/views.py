from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def data(request):
    return HttpResponse("<h1>ВИКТОРИНА</h1>" 
                        "<h3>ВОПРОС: Почему утки плавают</h3>"
                        "<h6>(ответ на странице test</h6>")

def test(request):
    return HttpResponse("<p>Ответ: Потому, что у них лапы красные</p>")
