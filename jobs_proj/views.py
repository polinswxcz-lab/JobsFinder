import requests

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.conf import settings

from .models import Vacancy
from .forms import VacancyForm


# ---------------- HOME ----------------
def home(request):
    vacancies = Vacancy.objects.all()[:6]

    return render(request, "jobs_proj/index.html", {
        "vacancies": vacancies
    })


# ---------------- LIST + SEARCH + PAGINATION ----------------
def vacancies_list(request):

    qs = Vacancy.objects.all()

    search = request.GET.get("q", "")

    if search:
        qs = qs.filter(title__icontains=search)

    paginator = Paginator(qs, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "jobs_proj/vacancies.html", {
        "page_obj": page_obj,
        "search": search
    })


# ---------------- DETAIL ----------------
def vacancy_detail(request, id):

    vacancy = get_object_or_404(Vacancy, id=id)

    return render(request, "jobs_proj/detail.html", {
        "vacancy": vacancy
    })


# ---------------- CREATE ----------------
def add_vacancy(request):

    if request.method == "POST":
        form = VacancyForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("vacancies")

    else:
        form = VacancyForm()

    return render(request, "jobs_proj/add_vacancy.html", {
        "form": form
    })


# ---------------- UPDATE ----------------
def update_vacancy(request, id):

    vacancy = get_object_or_404(Vacancy, id=id)

    form = VacancyForm(request.POST or None, instance=vacancy)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("vacancies")

    return render(request, "jobs_proj/add_vacancy.html", {
        "form": form
    })


# ---------------- DELETE ----------------
def delete_vacancy(request, id):

    vacancy = get_object_or_404(Vacancy, id=id)

    if request.method == "POST":
        vacancy.delete()
        return redirect("vacancies")

    return render(request, "jobs_proj/delete.html", {
        "vacancy": vacancy
    })


# ---------------- API IMPORT (JOOBLE) ----------------
def parse_jooble(request):

    url = f"https://jooble.org/api/{settings.JOOBLE_API_KEY}"

    payload = {
        "keywords": "python developer",
        "location": "Ukraine"
    }

    response = requests.post(url, json=payload)
    data = response.json()

    for item in data.get("jobs", []):
        Vacancy.objects.update_or_create(
            source_url=item.get("link"),
            defaults={
                "title": item.get("title"),
                "company": item.get("company"),
                "location": item.get("location"),
                "description": item.get("snippet"),
                "salary": 0
            }
        )

    return redirect("vacancies")


# ---------------- ABOUT ----------------
def about(request):
    return render(request, "jobs_proj/about.html")