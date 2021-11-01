from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index')
]

urlpatterns += [
    url(r'^books/$', views.BookListView.as_view(), name='books')
]

urlpatterns += [
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')
]

urlpatterns += [
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors')
]

urlpatterns += [
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail')
]

urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]

urlpatterns += [
    url(r'^all-borrowed-books/', views.AllBorrowedBooks.as_view(), name='all-borrowed-books'),
]
