from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article


def articles(request):
    articles = Article.objects.all().order_by("-created_at")
    context = {"articles": articles, }
    return render(request, "articles.html", context)


def new(request):
    return render(request, "new.html")


def create(request):

    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article(title=title, content=content)
    article.save()
    context = {
        "article": article,
    }
    return redirect("products:articles")


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {"article": article}
    return render(request, "detail.html", context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect("products:articles")


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "edit.html", context)


def update(request, pk):
    title = request.POST.get("title")
    content = request.POST.get("content")

    article = Article.objects.get(pk=pk)
    article.content = content
    article.title = title
    article.save()
    return redirect("products:detail", article.pk)
