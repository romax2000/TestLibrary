from django.conf.urls import url
from django.urls import path, include


#from app.views import base_view
from app.views import book_view
from app.views import edit_view


from app.views import BaseListView
from app.views import BaseDetailView
from app.views import BaseFormView

urlpatterns = [
#url(r'^book/(?P<user_id>[-\w]+)/$', book_view, name='user_books'),
url(r'^edit_book/(?P<pk>[-\w]+)/$', edit_view, name='edit_book'),
#url(r'^$', base_view, name='base'),
url(r'^book/(?P<pk>[-\w]+)/$', BaseDetailView.as_view(), name = 'user_books'),
url(r'^$', BaseFormView.as_view(), name = 'base'),
url(r'^$', BaseListView.as_view(), name = 'base'),
]