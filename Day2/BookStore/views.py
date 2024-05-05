from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


def index(request):
    return render(request, "main/base_layout.html")


def book_list(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "bookstore/book_list.html", context=context)


def book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {"book": book}
    return render(request, "bookstore/book_details.html", context=context)


def book_delete(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("bookstore:book-list")


def book_update(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.description = request.POST.get("description")
        book.rate = request.POST.get("rate")
        book.views = request.POST.get("views")
        book.save()
        return redirect("bookstore:book-list")
    else:
        context = {"book": book}
        return render(request, "bookstore/book_update.html", context=context)


def book_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        rate = request.POST.get("rate")
        views = request.POST.get("views")
        if title and description and rate and views:
            new_book = Book.objects.create(
                title=title,
                description=description,
                rate=rate,
                views=views,
            )
            return redirect("bookstore:book-list")
    else:
        return render(request, "bookstore/book_create.html")
