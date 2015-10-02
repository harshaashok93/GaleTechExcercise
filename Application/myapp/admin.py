from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	#fields = ['author', 'book_title', 'pub_date', 'category']
	list_display = ["book_title","author","pub_date","category","book_image","book_description"]
	list_filter = ["pub_date"]
	search_fields = ['book_title']

admin.site.register(Article, ArticleAdmin)
