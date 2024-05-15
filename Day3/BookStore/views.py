from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Book, Category
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import permission_required


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "categories"]

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if len(title) < 10 or len(title) > 50:
            raise ValidationError("Title must be between 10 and 50 characters.")
        return title

    def clean_categories(self):
        categories = self.cleaned_data.get("categories")
        if len(categories) < 1:
            raise ValidationError("Please select at least one categories.")
        return categories


def index(request):
    return render(request, "main/base_layout.html")


@login_required
def book_list(request):
    books = Book.objects.all()
    user = request.user
    return render(request, "bookstore/book_list.html", {"books": books, "user": user})


def book_details(request, isbn_number):
    book = get_object_or_404(Book, isbn_number=isbn_number)
    context = {"book": book}
    return render(request, "bookstore/book_details.html", context=context)


@login_required
@permission_required("BookStore.delete_book", raise_exception=True)
def book_delete(request, isbn_number):
    book = get_object_or_404(Book, isbn_number=isbn_number)
    book.delete()
    return redirect("bookstore:book-list")


@login_required
def book_update(request, isbn_number):
    book = get_object_or_404(Book, isbn_number=isbn_number)
    categories = Category.objects.all()
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("bookstore:book-list")
    else:
        form = BookForm(instance=book)
        selected_category_ids = book.categories.values_list("id", flat=True)
        form.fields["categories"].initial = list(selected_category_ids)
    return render(
        request, "bookstore/book_update.html", {"form": form, "categories": categories}
    )


@login_required
def book_create(request):
    categories = Category.objects.all()

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = request.user
            new_book = form.save(commit=False)
            new_book.user = user
            new_book.save()
            form.save_m2m()
            return redirect("bookstore:book-list")
    else:
        form = BookForm()
    return render(
        request, "bookstore/book_create.html", {"form": form, "categories": categories}
    )


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("bookstore:book-list")
    else:
        form = AuthenticationForm()
    return render(request, "bookstore/login.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("bookstore:book-list")
    else:
        form = UserCreationForm()
    return render(request, "bookstore/signup.html", {"form": form})
