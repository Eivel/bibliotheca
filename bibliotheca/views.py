from django.shortcuts import render
from django.views.generic import View, ListView
from django.http import HttpResponseRedirect
from bibliotheca.models import *
from bibliotheca.forms import ReadersForm, UserCreateForm

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
    def get(self, request, *args, **kwargs):
        category = Categories.objects.all()
        authors = Authors.objects.all()
        books = Books.objects.all()
        books_authors = Books_Authors.objects.all()
        multiple_authors = {}
        for book in books:
            multiple_authors[book.title] = []
            for b_a in books_authors:
                if b_a.book_id.pk == book.pk:
                    multiple_authors[book.title].append(b_a.author_id)


        context = {
            'books' : books,
            'authors' : multiple_authors
        }

        return render(request,self.template, context)