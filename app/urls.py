from django.conf.urls import url, include
from django.urls import path

from app.views import base_view, edit_user_view, remove_user_view, book_view, edit_book_view, remove_book_view

from app.api.views import UserView

urlpatterns = [
    url(r'^book/(?P<user_id>[-\w]+)/$', book_view, name='user_books'),
    url(r'^edit_book/(?P<book_id>[-\w]+)/$', edit_book_view, name='edit_book'),
    url(r'^remove_book/(?P<book_id>[-\w]+)/$', remove_book_view, name='remove_book'),
    url(r'^edit_user/(?P<user_id>[-\w]+)/$', edit_user_view, name='edit_user'),
    url(r'^remove_user/(?P<user_id>[-\w]+)/$', remove_user_view, name='remove_user'),
    url(r'^users/$', UserView.as_view()),
    path('users/<int:pk>', UserView.as_view()),
    url(r'^$', base_view, name='base')
]
