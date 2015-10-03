from django.shortcuts import render

from .admin import ArticleAdmin
from .models import Article, Magazine

# Create your views here.

def home(request):
		
	
	return render(request, "myapp/home.html", {'a':Article.objects.all(),
		'b': Magazine.objects.all()})

def display(request, book_id):

	context = { 'art' : Article.objects.get(book_title = book_id),
				 'a'  : Article.objects.all(),
				 'b': Magazine.objects.all(),
			  }
	#this return a row containing all the tuple like book-title, author, book_image, pub_date etc

	return render(request, "myapp/display.html", context)
	#passing context as a parameter to my display.html template