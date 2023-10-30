from .forms import AddBlankForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from .parse_core import ParseResult
from redis_app.redis_repository import RedisRepository
from bookmark_project.tasks import task_get_tags


def get_url(request):
    """Функция отображения и взаимодействия с формой для добавления закладки"""
    if request.method == 'POST':
        form = AddBlankForm(request.POST)

        if form.is_valid():
            connection = RedisRepository()
            # creation_bookmark = ParseResult(request.POST['url'])
            data_for_db = task_get_tags.delay(request.POST['url'])
            connection.set_dict(request.POST['url'])
            return HttpResponseRedirect('success')
    else:
        form = AddBlankForm()
    return render(request, 'parse/create_bookmark.html', {'form': form})


# def get_list_bookmarks(request):
#     """Функция отображения списка закладок"""
#     connection = RedisRepository()
#     data = connection.get_list_dict()
#     return render(request, 'parse/list_of_bookmarks.html', {'list_of_bookmarks': data})


class ListBookmarks(ListView):
    """Класс отображения списка закладок"""
    template_name = 'parse/list_of_bookmarks.html'
    context_object_name = 'list_of_bookmarks'

    def get_queryset(self):
        connection = RedisRepository()
        return connection.get_list_dict()


def successful_addition(request):
    """Функция отображения страницы успешного добавления ссылки для парсинга"""
    return render(request, 'parse/success.html')
