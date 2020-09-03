from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from ..decorators import webuser_required
from ..forms import WebUserSignUpForm, DocumentForm, RatingsForm
from ..models import WebUser, User, EmployerDetails, ApplicationData, Application, Ratings
from django.core.files.storage import FileSystemStorage
from django.db.models import Q

from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

#importing get_template from loader
from django.template.loader import get_template
from django.db.models import Sum, Avg
#import render_to_pdf from util.py 
from ..utils import render_to_pdf
from django.views.generic import View

from django.core.mail import send_mail, BadHeaderError

# Create your views here.

def downloadtemplate(request):
    return render(request, "download_resume_template.html")




class WebUserSignUpView(CreateView):
    model = User
    form_class = WebUserSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'webuser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('webuser:userhome')


@webuser_required
def userhome(request):
    context = {
        "employerdetails": EmployerDetails.objects.all(),

    }
    return render(request, "userhome.html", context)



@webuser_required
def infopage(request):
    context = {
        "employerdetails": EmployerDetails.objects.all(),

    }
    return render(request, "infopage.html", context)



@webuser_required
def specificcompanypage(request, company_name):
    context = {
        "details": EmployerDetails.objects.filter(company_name=company_name),
     #   "Total":list(Ratings.objects.filter(company_name=company_name).Avg(Sum('rating')).values())[0],
        "Total": Ratings.objects.filter(company_name=company_name).aggregate(rating = Avg('rating')),
        "ratings": Ratings.objects.filter(company_name=company_name),
    #specificcompanypage=Document(employer_name=employer_name)    
    #specificcompanypage.save() 
    }
    return render(request, "specific_company_page.html", context)


@webuser_required
def rate(request, company_name):
    context = {
     
        "ratings": Ratings.objects.filter(company_name=company_name),
    #specificcompanypage=Document(employer_name=employer_name)    
    #specificcompanypage.save() 
    }
    return render(request, "viewratings.html", context)





@webuser_required
def searchposts(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(company_name__icontains=query) 

            results= EmployerDetails.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'userhome.html', context)

        else:
            return render(request, 'userhome.html')

    else:
        return render(request, 'userhome.html')





@webuser_required
def sendmail(request):
    if request.method == 'GET':
        form = DocumentForm()
    else:
         ctx = {
        'user': "Admin"
        }
         

         form = DocumentForm(request.POST, request.FILES)
         if form.is_valid():
            subject = form.cleaned_data['company_name']
            from_email = form.cleaned_data['email']
            message = get_template('mail.html').render(ctx)
            
           
            form.save()
            try:
                msg = send_mail(subject, message, from_email, ['admin@example.com'])
            #    msg.content_subtype = "html"  # Main content is now text/html
             #   msg.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('webuser:userhome')
    return render(request, "apply.html", {'form': form})



class RatingsView(CreateView):
    model = Ratings
    form_class = RatingsForm
    template_name = 'ratecompany.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'webuser'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        if form.is_valid:
            quote = form.cleaned_data.get('company_name')
            if EmployerDetails.objects.filter(company_name=quote).exists():
                user = form.save()
    
                return redirect('webuser:userhome')
            else:
                message = 'Object'
                return redirect('webuser:Ratings')







