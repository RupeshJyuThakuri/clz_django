from django.contrib import admin
from .models import Course, Category, Book, Student, Library
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display= ['bookId','book_name']

class LibraryAdmin(admin.ModelAdmin):
    list_display= ['book_id','student','expiry_date']

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(Student)
admin.site.register(Library, LibraryAdmin)