from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.view_book_list, name='book_list'),
]