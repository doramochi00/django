from django.http import HttpResponse
from django.shortcuts import render
from .models import book_list
from django_datatables_view.base_datatable_view import BaseDatatableView

def index(request):
    return render(request, 'test_app/index.html')

def view_book_list(request):
    data = book_list.objects.all()
    contents = {'data': data}
    return render(request, 'test_app/book_list.html', contents)

class DataTableView(BaseDatatableView):
    # モデルの指定
    model = book_list
    # 表示するフィールドの指定
    columns = ['book_name', 'author', 'publisher', 'price']

    # 検索方法の指定：部分一致
    def get_filter_method(self):
        return super().FILTER_ICONTAINS