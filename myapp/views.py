from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum,Q



def index(request):
  author = Author.objects.all().filter(popularity_score__gte = 50)
  author1 = author.first()
  author2 = author.last()
  print(author)
  print(author1)
  print(author2)
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
