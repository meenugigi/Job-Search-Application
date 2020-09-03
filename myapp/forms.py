from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from .models import (WebUser, User)
from .decorators import employer_required
from .models import Application, EmployerDetails, AvailablePosts, Ratings

class EmployerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employer = True
        if commit:
            user.save()
        return user


class WebUserSignUpForm(UserCreationForm):   
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_webuser = True
        user.save()
        student = WebUser.objects.create(user=user)
       
        return user


FRESHER_CHOICES = [
    ('yes', 'YES'),
    ('no', 'NO'),
   
    ]

class DocumentForm(forms.ModelForm):
    fresher= forms.CharField(label='Are you a fresher?', widget=forms.RadioSelect(choices=FRESHER_CHOICES))
    class Meta:
        model = Application
        fields = ('username','first_name','last_name', 'email', 'fresher','company_name', 'describe_yourself', 'resume',  )

    def save(self, user=None):
        user_profile = super(DocumentForm, self).save(commit=False)
        if user:
            user_profile.user = user
        user_profile.save()
        return user_profile





class EmployerForm(forms.ModelForm): 
        
    class Meta: 
        model = EmployerDetails
        fields = ('id','username', 'company_name', 'email', 'about_us','our_requirements', 'our_offical_website', 'companytype', 'availableposts', 'strength', 'vacancies',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['availableposts'].queryset = AvailablePosts.objects.none()

        if 'companytype' in self.data:
            try:
                companytype_id = int(self.data.get('companytype'))
                self.fields['availableposts'].queryset = AvailablePosts.objects.filter(companytype_id=companytype_id).order_by('names')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['availableposts'].queryset = self.instance.companytype.availableposts_set.order_by('names')





class RatingsForm(forms.ModelForm):  
    class Meta: 
        model = Ratings
        fields = '__all__'







