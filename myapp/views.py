from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum, Q, Min, Max, Avg



def index(request):
  author = Author.objects.all().aggregate(Avg('popularity_score'))
  print(author)
  res = ''
  for i,j in author.items():
    res += f'<h3>{i}: {round(j,2)}</h3>'
  return HttpResponse(res)
