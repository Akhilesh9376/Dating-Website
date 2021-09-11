from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.Login,name='login'),
    path('Home',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('signup',views.signup,name='signup'),
    path('member',views.member,name='member'),
    path('profile',views.profile,name='profile'),
    path('proceed',views.proceed,name="proceed"),
    path('logout_request',views.logout_request,name="logout_request"),
    path('blog',views.blog,name='blog'),
    path('blog/post/<int:post_id>/', views.post, name="post"),

    # for resetting password with the help of email
   
     path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="App1/password/password_reset.html"),
     name="reset_password"),

     path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="App1/password/password_reset_sent.html"), 
        name="password_reset_done"),

     path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="App1/password/password_reset_form.html"), 
     name="password_reset_confirm"),

     path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="App1/password/password_reset_done.html"), 
        name="password_reset_complete"),

        
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''
