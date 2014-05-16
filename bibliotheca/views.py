from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View
from bibliotheca.models import News
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView
from django.template import RequestContext, loader
# Create your views here.

class MyView(View):
    template = 'myview.html'
    def get(self, request, *args, **kwargs):
        #return HttpResponse(self.template.render())
        return render(request,self.template)

class NewsView(View):
    template = 'news.html'
    def get(self, request, *args, **kwargs):
        latest_news = News.objects.order_by('-creation_date')
        context = {
            'latest_news' : latest_news
        }
        return render(request,self.template, context)

class ContactView(View):
    template = 'contact.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template)

def index(request):
    return redirect(NewsView.as_view())