from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('contact', contact),
    path('protectionDesEnfants', enfant),
    path('levothyrox', levothyrox),
    path('description', description),
    path('honoraires', honoraires),
    path('articles', ArticlesListView.as_view()),
    path('article/<int:pk>', articleDetailView)
]
