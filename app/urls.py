from django.conf.urls import url


from app.views import base_view
from app.views import book_view
from app.views import edit_view
from app.api_crud import api_all_users
from app.api_crud import api_new_user
from app.api_crud import api_update_user
from app.api_crud import api_delete_user

urlpatterns = [
    url(r'^book/(?P<user_id>[-\w]+)/$', book_view, name='user_books'),
    url(r'^edit_book/(?P<book_id>[-\w]+)/$', edit_view, name='edit_book'),
    url(r'^all/$', api_all_users, name='api_all_users'),
    url(r'^new/$', api_new_user, name='api_new_user'),
    url(r'^update/$', api_update_user, name='api_update_user'),
    url(r'^delete/$', api_delete_user, name='api_delete_user'),
    url(r'^$', base_view, name='base'),
]
