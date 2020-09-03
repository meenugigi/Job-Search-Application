from django.urls import path
from django.conf.urls import url
from . import views
from django.urls import path, include
from .views import common, webuser, employer

urlpatterns = [
    
    path('', common.home, name='home'),

    path('webuser/', include(([
        path('userhome', webuser.userhome, name="userhome"),   
        path('specificcompanypage/<str:company_name>', webuser.specificcompanypage, name="specificcompanypage"),   
      #  path('apply', webuser.media_upload, name='media_upload'),
        path('search', webuser.searchposts, name='searchposts'),
        path('sendmail', webuser.sendmail, name='sendmail'),
        path('giveratings', webuser.RatingsView.as_view(), name="Ratings"),
        path('viewratings/<str:company_name>', webuser.rate, name="rate"),
      path('companydetails', webuser.infopage, name='infopage'),
        path('pdfs/', webuser.downloadtemplate, name="downloadtemplate"), 

    ], 'classroom'), namespace='webuser')),
   
  
    


    path('employer/', include(([
        path('employerhome', employer.employerhome, name="employerhome"),      
        path('employerform', employer.EmployerFormView.as_view(), name="employerform"),
        path('ajax/filteravailableposts/', employer.filteravailableposts, name='ajaxfilteravailableposts'),
      # path('applications-received/<str:company_name>', employer.applications_received, name='applications_received'),
        path('filterapplications', employer.ApplicationsReceivedListView.as_view(), name="filterapplications"),
          path('specificcompanypage/<str:company_name>', employer.specific_companypage_employer, name="specific_companypage_employer"),
        path('update/<int:pk>/', employer.EmployerFormUpdateView.as_view(), name='update_form'),
        path('delete/<int:pk>/', employer.EmployerFormDeleteView.as_view(), name='delete_form'),
        path('mycompanyratings', employer.CompanyRatingsListView.as_view(), name="mycompanyratings"),
   




    ], 'classroom'), namespace='employer')),

]