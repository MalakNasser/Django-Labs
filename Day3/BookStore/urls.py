from django.urls import path
from . import views

app_name = "bookstore"

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("book_list/", views.book_list, name="book-list"),
    path("book_details/<slug:isbn_number>/", views.book_details, name="book-details"),
    path(
        "book_delete/<slug:isbn_number>/delete/", views.book_delete, name="book-delete"
    ),
    path(
        "book_update/<slug:isbn_number>/update/", views.book_update, name="book-update"
    ),
    path("create/", views.book_create, name="book-create"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout, name="logout"),
]
