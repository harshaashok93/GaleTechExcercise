from django.contrib import admin

# Register your models here.

from .models import Article, Magazine

class ArticleAdmin(admin.ModelAdmin):
	#fields = ['author', 'book_title', 'pub_date', 'category']
	list_display = ["book_title","author","pub_date","category","book_image","book_description"]
	#displays the list of tuples displayed in the order specified in the list "list_display". It basically
	#display it like a form

	list_filter = ["pub_date"]
	#adds a filter on the side, which can be used to filter out based on the parameter set. i.e, pub_date

	search_fields = ['book_title']
	#adds a search field on top of the page, to search articles based on the parameter passed. Here which is book_title.

admin.site.register(Article, ArticleAdmin)

class MagazineArticle(admin.ModelAdmin):

	list_display = ["magazine_title", "magazine_image"]

admin.site.register(Magazine, MagazineArticle)
