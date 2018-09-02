from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticlesListView, self).get_context_data(**kwargs)
        articles = list(self.model.objects.all().values())[::-1]
        paginator = Paginator(articles, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            list_articles = paginator.page(page)
        except PageNotAnInteger:
            list_articles = paginator.page(1)
        except EmptyPage:
            list_articles = paginator.page(1)
        context['articles'] = list_articles
        return context


def articleDetailView(request, pk):
    art = get_object_or_404(Article, pk=pk)
    return render(request, "articles/detail_view.html", context={"article": art})

