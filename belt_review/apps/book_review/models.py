from __future__ import unicode_literals

from django.db import models

from ..users.models import User


class Author(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BookManager(models.Manager):
    def new(self, *args):
        book_title = args[0]['book_title']
        author_text = args[0]['author_text']
        select_author = args[0]['select_author']
        review = args[0]['review']
        rating = args[0]['rating']

        # The errors list is used to append any validiation errors found when
        # adding on a book and review.
        errors = []

        #print(book_title, author_text, select_author, review, rating)
        
        # Right now, I have the user id hardcoded for who is creating the
        # books. I need to bring in my request.session['id']
        user_id = 2

        # Check for author_text and length of author_text, or if the
        # select_author selection menu was used, ignore the author_text field.
        if not select_author and not author_text:
            errors.append("Please select an author.")
        elif author_text and len(author_text) < 1:
            errors.append("Author names must be at least one character.")

        # Check for book title and length of book title
        if not book_title:
            errors.append('Please add a book title.')
        elif len(book_title) < 1:
            errors.append("Book titles must be at least one character.")

        # Check for book review
        if not review:
            errors.append('A written review is required.')
        elif len(review) < 5:
            errors.append("Book reviews must be at least 5 characters.")

        # Check for a rating
        #if not rating:
            #errors.append("Please select a rating.")

        if errors:
            return (False, errors)
        else:
            current_user = User.objects.get(id=user_id)

            if not author_text:
                author_object = Author.objects.get(id=select_author)
            else:
                author_object = Author.objects.create(name=author_text
                        ,created_by=current_user)

            # The following line instantiates and saves a book object.
            book = Book.objects.create(book_title=book_title
                    , author=author_object
                    , created_by=current_user)
            # The following line instantiates and saves a review object.
            review = Review.objects.create(book=book, reviewed_by=current_user
                    , rating=rating, review=review)
            return (True, review)


class Book(models.Model):
    book_title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    created_by = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()


class Review(models.Model):
    book = models.ForeignKey(Book)
    reviewed_by = models.ForeignKey(User)
    rating = models.IntegerField()
    review = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
