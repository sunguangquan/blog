from django.shortcuts import render, HttpResponse
from .models import Blog
# Create your views here.
def home(request):
    context = {'blog':Blog.objects.all()}
    return render(request,'blog\home.html',context=context)