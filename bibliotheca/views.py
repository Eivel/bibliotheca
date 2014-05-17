from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
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
        if request.method == "POST":
            form_creation = UserCreateForm(request.POST)
            form_readers = ReadersForm(request.POST)

            if form_creation.is_valid() and form_readers.is_valid():
                msg = 'ok'
            else:
                msg = 'nie ok'
        else:
            form_creation = UserCreateForm()
            form_readers = ReadersForm()
            msg = 'brak'

        context = {
            'form_creation' : form_creation,
            'form_readers' : form_readers,
            'msg' : msg
        }

        return render(request, self.template, context)

    def post(self, request):
        form_creation = UserCreateForm(request.POST)
        form_readers = ReadersForm(request.POST)

        if form_creation.is_valid() and form_readers.is_valid():
            msg = 'ok'
        else:
            msg = 'nie ok'

        context = {
            'form_creation' : form_creation,
            'form_readers' : form_readers,
            'msg' : msg
        }

        return render(request, self.template, context)


