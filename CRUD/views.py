from django.shortcuts import render, redirect
from .models import Booklist

# Create your views here.

def index(request):
    booklist = Booklist.objects.all()
    data = {'books': booklist}
    return render(request, 'index.html', data)

def create(request):
    btitle = request.GET['title']
    bprice = request.GET['price']
    bauthor = request.GET['author']
    newBook = Booklist(title=btitle, author=bauthor, price=bprice)
    newBook.save()
    return redirect('/')


def add_book(request):
    return render(request, 'add_book.html')


def edit(request, id):
    book = Booklist.objects.get(pk=id)
    data = {'book': book}
    return render(request, 'edit.html', data)


def update(request, id):
    book = Booklist.objects.get(pk=id)
    book.title = request.GET['title']
    book.price = request.GET['price']
    book.author = request.GET['author']
    book.save()
    return redirect('/')



def delete(request, id):
    book = Booklist.objects.get(pk=id)
    book.delete()
    return redirect('/')