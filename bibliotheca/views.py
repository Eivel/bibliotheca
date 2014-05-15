from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic import ListView, CreateView
from django.views.generic import UpdateView
from django.template import RequestContext, loader
# Create your views here.

class MyView(View):
    template = 'myview.html'
    def get(self, request, *args, **kwargs):
        #return HttpResponse(self.template.render())
        return render(request,self.template)

