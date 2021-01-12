from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from demo.models import Book
# Create your views here.

class Another(View):

    def get(self,request):
        return HttpResponse('This is another function inside class')


def first(request):
    return HttpResponse('first')
