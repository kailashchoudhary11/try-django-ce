from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article

# Create your views here.

def article_search_view(request):
    # print(dir(request))
    print(request.GET)

    query_dict = request.GET 
    try:
        query = int(query_dict.get('query'))
    except:
        query = None

    article_obj = None
    if query is not None: 
        article_obj = Article.objects.get(id = query)
    context = {
        'object' : article_obj
    }
    return render(request, "articles/search.html", context=context)


@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        article_obj = form.save()
        # title = form.cleaned_data.get('title')
        # content = form.cleaned_data.get('content')
        # article_obj = Article.objects.create(title=title, content=content)
        # context['article'] = article_obj
        # context['created'] = True
        context['form'] = ArticleForm()
    countcasesensitive = Article.objects.filter(title__exact = 'kai').count()
    countcaseinsensitive = Article.objects.filter(title__iexact = 'kai').count()
    titleContainingKaiCaseSensitive = Article.objects.filter(title__contains = 'kai').count()
    titleContainingKaiCaseInSensitive = Article.objects.filter(title__icontains = 'kai').count()
    # print(countcasesensitive)
    # print(countcaseinsensitive)
    # print(titleContainingKaiCaseSensitive)
    # print(titleContainingKaiCaseInSensitive)
        
    return render(request, "articles/create.html", context=context) 


# @login_required
# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')
#             content = form.cleaned_data.get('content')
#             article_obj = Article.objects.create(title=title, content=content)
#             context['article'] = article_obj
#             context['created'] = True
#     return render(request, "articles/create.html", context=context) 

def article_detail_view(request, id = None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/detail.html", context=context) 