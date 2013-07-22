from django.db import models
from django.core.urlresolvers import reverse

class Author(models.Model):
    name	= models.CharField(max_length=100)
    bio		= models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return '/livros/%i'% self.pk

class Book(models.Model):
    title	 	= models.CharField(max_length=100)
    author	 	= models.ForeignKey(Author,)
    release		= models.TextField(blank=True, null=True)
    available	= models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detalhes-livro', kwargs={'pk':self.pk})



