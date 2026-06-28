from django.urls import path
from .views import *

urlpatterns = [

path(
"",
home,
name="home"
),

path(
"vacancies/",
vacancies,
name="vacancies"
),

path(
"vacancy/<int:id>/",
vacancy_detail,
name="vacancy_detail"
),

path(
"articles/",
articles,
name="articles"
),

path(
"articles/<int:id>/",
article_detail,
name="article_detail"
),

path(
"add-article/",
add_article,
name="add_article"
),

path(
"about/",
about,
name="about"
),

]