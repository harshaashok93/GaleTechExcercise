from __future__ import unicode_literals
from django.db import models


class Article(models.Model):
    book_title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    pub_date = models.DateField('Published On')
    category = models.CharField(max_length=20)
    book_image = models.CharField(default="(book_title.jpg)", max_length=50)
    book_description = models.CharField(default="(give description...)",
                                        max_length=1000)

    def __unicode__(self):
        return self.book_title
