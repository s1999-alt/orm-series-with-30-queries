from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum



def index(request):
  author = Books.objects.all().filter(author__popularity_score__gte = 7).aggregate(total_price = Sum('price'))
  print(author)
  res = ''
  for i,j in author.items():
    res += f'<h3>{i}: {j}</h3>'
  return HttpResponse(res)
