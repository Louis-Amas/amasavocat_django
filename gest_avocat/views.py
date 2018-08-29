from django.shortcuts import render, get_object_or_404
from .models import Article
from django.views.generic import ListView, DetailView
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def contact(request):
    return render(request, "pages/contact.html")


def honoraires(request):
    return render(request, "pages/honoraires.html")


def levothyrox(request):
    return render(request, "pages/levothyrox.html")


def description(request):
    return render(request, "pages/description.html")


class ArticlesListView(ListView):

    model = Article

    context_object_name = 'articles'
    template_name = "articles/list_view.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        return {"articles": list(self.model.objects.all().values())[::-1]}


def articleDetailView(request, pk):
    art = get_object_or_404(Article, pk=pk)
    return render(request, "articles/detail_view.html", context={"article": art})

