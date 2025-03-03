from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddArticle, CommentForm
from .models import Article


def index(request):
    articles = Article.objects.all()
    return render(request, 'main/index.html', {'articles': articles})

@login_required
def add_article(request):
    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            try:
                Article.objects.create(**form.cleaned_data)
                Article.author = request.user
                return redirect('index')
            except Exception as e:
                print(f"Ошибка при добавлении статьи: {e}")
                form.add_error(None, f"Ошибка добавления статьи: {e}")
    else:
        form = AddArticle()
    return render(request, 'main/add_article.html', {'form': form})


@login_required
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user
            comment.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = CommentForm()

    return render(request, 'main/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    # Проверяем, является ли текущий пользователь автором статьи
    if request.user != article.author:
        return redirect('index')  # Перенаправляем, если пользователь не автор

    if request.method == 'POST':
        form = AddArticle(request.POST)
        if form.is_valid():
            Article.objects.create(**form.cleaned_data)
            return redirect('main/article_detail', article_id=article.id)
    else:
        form = AddArticle()

    return render(request, 'main/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.user != article.author:
        return redirect('index')

    if request.method == 'POST':
        article.delete()
        return redirect('index')

    return render(request, 'main/confirm_delete.html', {'article': article})



