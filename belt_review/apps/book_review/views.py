from django.shortcuts import render, redirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages

from .models import Book, Review, Author
from ..users.models import User

def index(request):
    reviews = Review.objects.all()
    authors = Author.objects.all()
    context = { 'authors': authors, 'reviews': reviews }
    return render(request, "book_review/index.html", context)

def new(request):
    authors = Author.objects.all()
    context = { 'authors': authors }
    return render(request, "book_review/new.html", context)

def create(request):
    if request.method == 'POST':
        try:
            #print('try')
            return_tuple = Book.objects.new(request.POST)
            if return_tuple[0] == True:
                # If return_tuple[0] is True, the object has been created and
                # added to the database.
                messages.success(request, "You've added a book!")
                return redirect(reverse('books:index'))
            else:
                # Return with error messages after validation
                messages.error(request, return_tuple[1])
                return redirect(reverse('books:new'))
        except:
            # Once I'm done with development, there really isn't a reason a
            # user should get into this except unless they are messing with my
            # site.
            messages.error(request,"Unable to create object.")
            return redirect(reverse('books:new'))
    else:
        messages.error(request, "wrong http method")
        return redirect(reverse('books:new'))

def show(request, book_id):
    book = Book.objects.get(id=book_id)
    context = { 'book': book }
    return render(request, "book_review/book.html", context)

def review(request, book_id):
    book = Book.objects.get(id=book_id)
    return redirect(reverse('books:index'))
