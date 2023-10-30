from django.urls import path
from .views import get_url, successful_addition, ListBookmarks

urlpatterns = [
    path('', get_url, name='main_parse'),
    path('success', successful_addition, name='success'),
    path('bookmark_list', ListBookmarks.as_view(), name='bookmarks_list')
]
