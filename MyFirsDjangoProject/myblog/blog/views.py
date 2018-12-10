from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    articles = models.Acticle.objects.all()
    return render(request, 'index.html', {'articles':articles})

def article_page(request, article_id):
    article = models.Acticle.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article':article})

def article_edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'article_edit_page.html')
    article = models.Acticle.objects.get(pk=article_id)
    return render(request, 'article_edit_page.html', {'article':article})

def article_edit_page_action(request):
    title = request.POST.get('title', '默认标题')
    content = request.POST.get('content', '默认内容')
    article_id = request.POST.get('article_id_hidden', '0')

    if str(article_id) == '0':
        models.Acticle.objects.create(title=title, content=content)
        articles = models.Acticle.objects.all()
        return render(request, 'index.html', {'articles': articles})
    article = models.Acticle.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'article_page.html', {'article':article})