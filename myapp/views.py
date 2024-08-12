from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User



def index(request):
  author =Author.objects.all().filter(joindate__year__gte=2013)
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
