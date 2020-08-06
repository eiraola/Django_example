from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,

)
class ArticleListView(ListView):
    template_name = 'blog_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    queryset = Article.objects.all()
# Create your views here.
def article_list(request):
    queryset = Article.objects.all()
    context = {
        'list': queryset
    }

    return render(request, "blog_list.html", context)

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()

    my_context = {
        'form': form
    }
    return render(request, "blog_create.html", my_context)

def article_lookup_view(request, my_id):
    try:
        obj: object = Article.objects.get(id=int(my_id))
    except Article.DoesNotExist:
        raise Http404
    # obj = get_object_or_404(product, id=my_id)

    context = {
        "obj": obj
    }
    return render(request, "article_detail.html", context)

