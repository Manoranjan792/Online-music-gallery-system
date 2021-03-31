from django.shortcuts import render
from django.http import HttpResponse
from .models import Song
from .forms import ContactForm
# Create your views here.
def index(request):
    #return render(request,'home/index.html')
    return HttpResponse("<h1 style='color:green;'>you are successfully login</h1><a href='services'>Services</a> <br> <a href='aboutus'>About Us </a>")

def aboutus(request):
    #return render(request,'home/aboutus.html')
    return HttpResponse("<h1 style='color:green;'>welcome, My name is Manoranjan Panday</h1><a href='../services'>Services</a> <br> <a href='..'>Home</a>")
def services(request):

    return HttpResponse("<h1 style='color:green;'>welcome to Services Page</h1> <a href='../aboutus'>About Us</a> <br> <a href='..'>Home</a>")

def songdetails(request):
    songsdata=Song.objects.all()
    return render(request,'home/songdetails.html',{'songs':songsdata})
def contact(request):
    contactform = ContactForm()
    return render(request,'home/contact.html',{'forms':contactform})

 
