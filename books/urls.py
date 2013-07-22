from django.conf.urls import patterns, url, include
from .views import (BooksListView, BooksCreateView, BooksDetailView, 
					BooksUpdateView, BooksDeleteView, AuthorCreateView)

urlpatterns = patterns('',
	url(r'^$', BooksListView.as_view(), name="livros"),
	url(r'^novo/$', BooksCreateView.as_view(), name='novo-livro'),
	url(r'^(?P<pk>\d+)/$', BooksDetailView.as_view(), name='detalhes-livro'),
	url(r'^(?P<pk>\d+)/atualizar/$', BooksUpdateView.as_view(), name='atualizar-livro'),
	url(r'^(?P<pk>\d+)/apagar/$', BooksDeleteView.as_view(), name='apagar-livro'),

	# Crud Author
	url(r'^novo/autor/$', AuthorCreateView.as_view(), name='novo-autor'),
	
	)