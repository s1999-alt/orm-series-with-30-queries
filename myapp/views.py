from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Books, Publisher, User



def index(request):
  author =Author.objects.all().order_by('-joindate').values_list('firstname','lastname','joindate').first()
  res = ''
  for i in author:
    res += f'<h3>{i}</h3>'
  return HttpResponse(res)
