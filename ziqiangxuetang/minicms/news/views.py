from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def index(request):
    columns = Column.objects.all()
    return render(request, 'index.html', locals())

def column_detail(request, slug):
	column = Column.objects.get(slug=slug)
	return render(request, 'news/column.html', locals())

def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	return render(request, 'news/article.html', locals())
