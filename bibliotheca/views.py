from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from bibliotheca.models import News
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

