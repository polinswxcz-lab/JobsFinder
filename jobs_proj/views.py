from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import (
    Vacancy,
    Article
)

from .forms import ArticleForm


def home(request):

    vacancies = Vacancy.objects.all()[:3]

    articles = Article.objects.all()[:3]

    return render(
        request,
        "jobs_proj/index.html",
        {
            "vacancies": vacancies,
            "articles": articles
        }
    )


def vacancies(request):

    vacancies = Vacancy.objects.all()

    return render(
        request,
        "jobs_proj/vacancies.html",
        {
            "vacancies": vacancies
        }
    )


def vacancy_detail(request, id):

    vacancy = get_object_or_404(
        Vacancy,
        id=id
    )

    return render(
        request,
        "jobs_proj/detail.html",
        {
            "vacancy": vacancy
        }
    )


def articles(request):

    articles = Article.objects.all()

    return render(
        request,
        "jobs_proj/articles.html",
        {
            "articles": articles
        }
    )


def article_detail(request, id):

    article = get_object_or_404(
        Article,
        id=id
    )

    return render(
        request,
        "jobs_proj/article_detail.html",
        {
            "article": article
        }
    )


def add_article(request):

    if request.method == "POST":

        form = ArticleForm(
            request.POST
        )

        if form.is_valid():

            form.save()

            return redirect(
                "articles"
            )

    else:

        form = ArticleForm()

    return render(
        request,
        "jobs_proj/add_article.html",
        {
            "form": form
        }
    )


def about(request):

    return render(
        request,
        "jobs_proj/about.html"
    )