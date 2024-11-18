from django.urls import path
from app.views import *

urlpatterns = [
    path("sample",sample),
    path("movie_review",movie_review),
    path("addlist",addlist),
]