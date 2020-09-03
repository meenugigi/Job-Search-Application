from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView, UpdateView, TemplateView)

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from ..decorators import employer_required
from ..forms import EmployerSignUpForm, EmployerForm
from ..models import User, EmployerDetails, AvailablePosts, Application, ApplicationData, Ratings

from django.http import HttpResponse
from ..utils import render_to_pdf
from django.views.generic import View
from django.db.models import Sum, Avg
# Create your views here.


class EmployerSignUpView(CreateView):
    model = User
    form_class = EmployerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('employer:employerhome')








@employer_required
def employerhome(request):
    context = {
        "employerdetails": EmployerDetails.objects.all(),


    }
    return render(request, "employerhome.html", context)


def specific_companypage_employer(request, company_name):
    context = {
        "details": EmployerDetails.objects.filter(company_name=company_name),
     #   "Total":list(Ratings.objects.filter(company_name=company_name).Avg(Sum('rating')).values())[0],
        "Total": Ratings.objects.filter(company_name=company_name).aggregate(rating = Avg('rating')),
        "ratings": Ratings.objects.filter(company_name=company_name),
    #specificcompanypage=Document(employer_name=employer_name)    
    #specificcompanypage.save() 
    }
    return render(request, "specific_company_pages_employer.html", context)






class EmployerFormView(CreateView):
    model = EmployerDetails
    form_class = EmployerForm
    template_name = 'employerform.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'employer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
    #    login(self.request, user)
        return redirect('employer:employerhome')




class EmployerFormUpdateView(UpdateView):
    model = EmployerDetails
    form_class = EmployerForm
    template_name = 'employerform.html'
    success_url = reverse_lazy('employer:employerhome')

    def get_context_data(self, **kwargs):
    #    kwargs['questions'] = self.get_object().questions.annotate(answers_count=Count('answers'))
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        '''
        This method is an implicit object-level permission management
        This view will only match the ids of existing quizzes that belongs
        to the logged in user.
        '''
        return self.request.user.company_name.all()

    def get_success_url(self):
        return reverse('employer:update_form', kwargs={'pk': self.object.pk})




class EmployerFormDeleteView(DeleteView):
 
    model = EmployerDetails
    context_object_name = 'quiz'
    template_name = 'employerform_delete_confirm.html'
    success_url = reverse_lazy('employer:employerhome')

    def delete(self, request, *args, **kwargs):
        remove = self.get_object()
        messages.success(request, 'The quiz %s was deleted with success!' % remove.company_name)
        return super().delete(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.company_name.all()








@employer_required
def specificcompanypage(request, company_name):
    context = {
        "details": EmployerDetails.objects.filter(company_name=company_name),
        
    }
    return render(request, "specific_company_page.html", context)




@employer_required
def filteravailableposts(request):
    companytype_id = request.GET.get('companytype')
    filterposts = AvailablePosts.objects.filter(companytype_id=companytype_id).order_by('names')
    return render(request, 'filterby_availableposts.html', {'filterposts': filterposts})





@employer_required
class PersonListView(ListView):
    model = EmployerDetails
    context_object_name = 'people'



@employer_required
class PersonCreateView(CreateView):
    model = EmployerDetails
    #fields = ('employername', 'email', 'description', 'companytype', 'availableposts', 'employeecount', 'noofvacancy', 'last_modified')
    form_class = EmployerForm
    success_url = reverse_lazy('person_changelist')


@employer_required
class PersonUpdateView(UpdateView):
    model = EmployerDetails
    #fields = ('employername', 'email', 'description', 'companytype', 'availableposts', 'employeecount', 'noofvacancy', 'last_modified')
    form_class = EmployerForm
    success_url = reverse_lazy('person_changelist')












class ApplicationsReceivedListView(ListView):
    model = Application
    ordering = ('name', )
    context_object_name = 'company_name'
    template_name = 'filterapplications.html'

    def get_queryset(self):
        company_name = self.request.user.company_name.values_list('pk', flat=True)
     #   employer_interests = company_name.company_name.values_list('pk', flat=True)
      
        queryset = Application.objects.filter(company_name__in=company_name) 
           
        return queryset




class CompanyRatingsListView(ListView):
    model = Ratings
    ordering = ('name', )
    context_object_name = 'company_name'
    template_name = 'mycompanyratings.html'

    def get_queryset(self):
        company_name = self.request.user.company_name.values_list('pk', flat=True)
     #   employer_interests = company_name.company_name.values_list('pk', flat=True)
      
        queryset = Ratings.objects.filter(company_name__in=company_name) 
           
        return queryset




