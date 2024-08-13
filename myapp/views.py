from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum, Q, Min, Max, Avg



def index(request):
  oldest_author = Author.objects.all().aggregate(Min('joindate'))
  newest_author = Author.objects.all().aggregate(Max('joindate'))
  avg_pop_score = Author.objects.all().aggregate(Avg('popularity_score'))
  sum_price = Books.objects.all().aggregate(Sum('price'))

  ans29 = [oldest_author, newest_author, avg_pop_score, sum_price]
  print(ans29)
  res = ''
  for i in ans29:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
