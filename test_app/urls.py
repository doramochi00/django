from django.urls import path
from django.views.generic import TemplateView
from .views import DataTableView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book_list/', views.view_book_list, name='book_list'),
    path('book_list_datatables', TemplateView.as_view(template_name='test_app/book_list_datatables.html'), name='book_list_datatables'),
    path('data/', DataTableView.as_view()),
]