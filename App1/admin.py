from App1.models import Profile
from django.contrib import admin
from .models import Blog, Profile,Contact

# Register your models here.


class adminProfile(admin.ModelAdmin):
    list_display =['user','gender','lookingFor','age','phone']
admin.site.register(Profile,adminProfile)
#  name email subject phone message

class adminContact(admin.ModelAdmin):
    list_display =['name','email','subject','phone','message']

admin.site.register(Contact,adminContact)
admin.site.register(Blog)
    














































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































