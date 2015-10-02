from django.shortcuts import render
from .models import Article


def home(request):
    return render(request, "myapp/home.html", {'a': Article.objects.all()})


def display(request, book_id):
    context = Article.objects.get(book_title=book_id)
    # this return a row containing all the tuple like book-title, author,
    # book_image, pub_date etc

    return render(request, "myapp/display.html", {
        'context': context,
        'a': Article.objects.all()})
    # passing context as a parameter to my display.html template
