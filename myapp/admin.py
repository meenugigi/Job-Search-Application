from django.contrib import admin
from .models import User, WebUser, CompanyType, AvailablePosts, EmployerDetails, Application, Ratings
# Register your models here.



admin.site.register(User)
admin.site.register(WebUser)

admin.site.register(CompanyType)
admin.site.register(AvailablePosts)
admin.site.register(EmployerDetails)

admin.site.register(Application)
admin.site.register(Ratings)

