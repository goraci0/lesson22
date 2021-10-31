from django.shortcuts import render
from articles.models import Article

def home_page(request):
    art_one = Article.objects.first()
    return render(request,"articles/index.html",{'article':art_one})