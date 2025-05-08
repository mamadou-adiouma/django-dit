from django.shortcuts import render
from django.http import Http404

# Create your views here.

def home(request):
    return render(request, 'html/home.html')

def article(request):
    return render(request, 'html/article.html')

def blog(request):
    return render(request, 'html/blog.html')

def article_detail(request):
    return render(request, 'html/article-detail.html')

def error404(request, exception):
        return render(request, 'html/errors/not_found404.html', status=404)
