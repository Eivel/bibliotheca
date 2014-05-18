from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponseRedirect
from bibliotheca.models import *
from bibliotheca.forms import ReadersForm, UserCreateForm
from django.db.models import Q
import pdb;

# Create your views here.
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

class UserRegister(View):
    template = 'registration/register.html'
    def get(self, request):

        form_creation = UserCreateForm()
        form_readers = ReadersForm()

        context = {
            'form_creation' : form_creation,
            'form_readers' : form_readers,
        }

        return render(request, self.template, context)

    def post(self, request):
        form_creation = UserCreateForm(request.POST)
        form_readers = ReadersForm(request.POST)

        if form_creation.is_valid() and form_readers.is_valid():
            user = form_creation.save()
            profile = form_readers.save(commit=False)
            profile.user = user
            profile.save()
            return render(request, 'registration/registerSuccess.html')

        context = {
            'form_creation' : form_creation,
            'form_readers' : form_readers,
        }

        return render(request, self.template, context)

class CategoryView(ListView):
    template = 'categories.html'

    def flatten(nested):
        flat = list()
        def flatten_in(nested, flat):
            for i in nested:
                flatten_in(i, flat) if isinstance(i, list) else flat.append(i)
            return flat
        flatten_in(nested, flat)
        return flat

    def get(self, request, cid, *args, **kwargs):
        #books = Books.objects.filter(category_id=cid)

        current = Categories.objects.get(id=cid)
        related_cats = current.get_all_children()
        relcats = CategoryView.flatten(related_cats)

        queries = [Q(category=value) for value in relcats]

        query = queries.pop()

        for item in queries:
            query |= item

        books = Books.objects.filter(query)

        obj = current
        breadcrumbs = []
        while obj != None:
            breadcrumbs.append(obj)
            obj = obj.top_category

        breadcrumbs.reverse()

        children = Categories.objects.filter(top_category=current)

        if children.count() == 0:
            current = current.top_category
            children = Categories.objects.filter(top_category=current)

        context = {
            'books' : books,
            'breadcrumbs' : breadcrumbs,
            'current' : current,
            'children' : children,
            'cid' : int(cid)
        }

        return render(request,self.template, context)

class BookView(View):
    template = 'book.html'
    def get(self, request, bid, *args, **kwargs):
        book = Books.objects.get(id=bid)
        obj = book.category_id
        breadcrumbs = []

        breadcrumbs.append(book)

        while obj != None:
            breadcrumbs.append(obj)
            obj = obj.top_category
        breadcrumbs.reverse()

        context = {
            'book': book,
            'breadcrumbs': breadcrumbs
        }
        return render(request,self.template, context)