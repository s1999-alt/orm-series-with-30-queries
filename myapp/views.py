from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum, Q, Min



def index(request):
  author = Author.objects.all().aggregate(Min('joindate'))
  print(author)
  res = ''
  for i,j in author.items():
    res += f'<h3>{i}: {j}</h3>'
  return HttpResponse(res)
