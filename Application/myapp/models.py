from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
	book_title = models.CharField(max_length=200)
	author = models.CharField(max_length=50)
	pub_date = models.DateField('Publication Date')
	category = models.CharField(max_length=20)
	book_image = models.CharField(default="(book_title.jpg)",max_length=50)
	book_description = models.CharField(default="(give description...)",max_length=1000)

	def __unicode__(self):

		return self.book_title

class Magazine(models.Model):

	magazine_title = models.CharField(max_length=100)
	magazine_image = models.CharField(max_length=100)

	def __unicode__(self):

		return self.magazine_title