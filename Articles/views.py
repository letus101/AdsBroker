from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

def article_list(request):
    search_query = request.GET.get('search', '')
    category_query = request.GET.get('category', '')
    ville_query = request.GET.get('ville', '') 

    articles = Article.objects.all()
    if search_query:
        articles = articles.filter(name__icontains=search_query)
    if category_query:
        articles = articles.filter(category=category_query)
    if ville_query:
        articles = articles.filter(ville=ville_query) 

    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})
@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})
@login_required
def article_update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'articles/article_form.html', {'form': form})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        return redirect('article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': article})
