from django.conf.urls import url


from app.views import base_view
from app.views import book_view
from app.views import edit_view

urlpatterns = [
    url(r'^book/(?P<user_id>[-\w]+)/$', book_view, name='user_books'),
    url(r'^edit_book/(?P<book_id>[-\w]+)/$', edit_view, name='edit_book'),
    url(r'^$', base_view, name='base'),
]
