from django.urls import path
from . import views


urlpatterns = [

    path(
        "",
        views.home,
        name="home"
    ),

    path(
        "vacancies/",
        views.vacancies_list,
        name="vacancies"
    ),

    path(
        "vacancies/<int:id>/",
        views.vacancy_detail,
        name="vacancy_detail"
    ),

    path(
        "vacancies/add/",
        views.add_vacancy,
        name="add_vacancy"
    ),

    path(
        "vacancies/<int:id>/edit/",
        views.update_vacancy,
        name="update_vacancy"
    ),

    path(
        "vacancies/<int:id>/delete/",
        views.delete_vacancy,
        name="delete_vacancy"
    ),

    path(
        "import/",
        views.parse_jooble,
        name="parse_jooble"
    ),

    path(
        "about/",
        views.about,
        name="about"
    ),

]