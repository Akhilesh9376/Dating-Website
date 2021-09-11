
from django.contrib import admin
from django.urls import path,include 

admin.site.site_header ="Dating Hub"
admin.site.site_title ="Dating Hub Admin Panel"
admin.site.index_title="One Site Many Work"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('App1.urls'))
]
