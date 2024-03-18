from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
        
class Book(models.Model):
    bookId= models.CharField(max_length=100, unique=True)
    book_name =models.CharField(max_length=100)
    
    def __str__(self):
        return self.book_name

class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class Library(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    expiry_date = models.DateField()
