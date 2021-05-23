from django.http import HttpResponse
from django.shortcuts import render
from .models import book_list

def index(request):
    return render(request, 'test_app/index.html')

def view_book_list(request):
    data = book_list.objects.all()
    contents = {'data': data}
    return render(request, 'test_app/book_list.html', contents)
