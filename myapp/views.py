from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum



def index(request):
  author = Author.objects.all().values_list('firstname','recommendedby__firstname')
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
