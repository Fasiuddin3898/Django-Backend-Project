from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is homepage")
def about(request):
    return HttpResponse("This is about page")
def services(request):
    return HttpResponse("This is service page")
def contacts(request):
    return HttpResponse("This is contacts page")