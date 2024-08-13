from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum, Q, Min, Max, Count



def index(request):
  author = Author.objects.annotate(f_count=Count('followers')).filter(f_count__gt=1)
  print(author)
  res = ''
  for i in author:
    res += f'<h3>{i.firstname} : {i.f_count}</h3>'
  return HttpResponse(res)
