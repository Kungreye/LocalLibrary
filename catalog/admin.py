from django.contrib import admin

from catalog.models import Genre, Language, Book, BookInstance, Author


admin.site.register(Genre)
admin.site.register(Language)
# admin.site.register(Book)
# admin.site.register(BookInstance)
# admin.site.register(Author)


class BooksInline(admin.TabularInline):
    model = Book
    extra = 0


# register the admin class with the associated model
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Book)   # equals `admin.site.register()`
class BookAdmin(admin.ModelAdmin):
    # Can't directly specify `genre` in list_display because it is a ManyToManyField.
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )















