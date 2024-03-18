from django.shortcuts import render
from .models import Course, Category
# Create your views here.
def index(request):
    course = Course.objects.all()
    
    return render(request, 'index.html', {'coursename': course})

def category(request):
    category = Category.objects.all()
    return render(request,'category.html', {'category':category})

def courseDetail(request, slug):
    course = Course.objects.filter(slug=slug)
    return render(request,'coursedetails.html', {'course':course})
