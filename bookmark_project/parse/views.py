from .forms import AddBlankForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .parse_core import ParseResult
from redis_app.redis_repository import RedisRepository

def get_url(request):
    if request.method == 'POST':
        form = AddBlankForm(request.POST)

        if form.is_valid():
            connection = RedisRepository()
            creation_bookmark = ParseResult(request.POST['url'])
            data_for_db = creation_bookmark.get_tags()
            connection.set_dict(request.POST['url'], data_for_db)
            return HttpResponseRedirect('success')
    else:
        form = AddBlankForm()
    return render(request, 'parse/create_bookmark.html', {'form': form})


def get_list_bookmarks(request):
    connection = RedisRepository()
    data = connection.get_list_dict()
    return render(request, 'parse/list_of_bookmarks.html', {'list_of_bookmarks': data})

class ListBookmarks(ListView):
    template_name = 'parse/list_of_bookmarks.html'
    context_object_name = 'list_of_bookmarks'

    def get_queryset(self):
        connection = RedisRepository()
        data = connection.get_list_dict()
        return connection.get_list_dict()

def successful_addition(request):
    return render(request, 'parse/success.html')
