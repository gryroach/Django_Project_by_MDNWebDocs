from django.contrib import admin
from django.urls.base import clear_script_prefix
from .models import Genre, Book, BookInstance, Author, Language
# Register your models here.

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# admin.site.register(Book)
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

# admin.site.register(BookInstance)
# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Genre)
admin.site.register(Language)
