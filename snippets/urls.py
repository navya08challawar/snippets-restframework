from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework import renderers

# API endpoints
urlpatterns = format_suffix_patterns([
    url('', views.api_root),
    url('snippets/',
        views.SnippetList.as_view(),
        name='snippet-list'),
    url('snippets/<int:pk>/',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),
    url('snippets/<int:pk>/highlight/',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    url('users/',
        views.UserList.as_view(),
        name='user-list'),
    url('users/<int:pk>/',
        views.UserDetail.as_view(),
        name='user-detail')
])
