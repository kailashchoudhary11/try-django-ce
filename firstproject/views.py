'''
To render html web pages
'''
from multiprocessing import context
import random
from pipes import Template
from turtle import title
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article

def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    name = "Kai"  # hard coded
    random_id = random.randint(1, 5) # pseudo random

    # from the database??
    article_obj = Article.objects.get(id = 9)
    article_queryset = Article.objects.all()

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content, 
        "object_list": article_queryset
    }
    
    # Django Template 
    HTML_STRING = render_to_string(
        "home-view.html",
        context = context
    )

    # HTML_STRING = """
    # <h1>{title} {id}</h1>
    # <p>{content}</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING) 