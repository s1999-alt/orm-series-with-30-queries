from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User
from django.db.models import Sum,Q



def index(request):
  author = Author.objects.filter(Q(firstname__istartswith='a') and (Q(popularity_score__gte=5) or Q(joindate__year__gt=2014)))
  print(author)
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
