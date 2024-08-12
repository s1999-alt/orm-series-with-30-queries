from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum



def index(request):
  author = Books.objects.all().filter(author__pk__in=[1, 3, 4]).aggregate(total=Sum('price'))
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
