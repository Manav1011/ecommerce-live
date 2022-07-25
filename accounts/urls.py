from django.urls import path,re_path
from . import views

app_name='accounts'

urlpatterns=[
    re_path(r'^$',views.SignupProcess.SignUpView,name='signup'),    
    path('active/<str:username>/<str:token>',views.SignupProcess.active_account,name='active'),
    re_path(r'^Activated/$',views.SignupProcess.activated,name='activated'),
    re_path(r'^Expired/$',views.SignupProcess.the_link_has_been_expired,name='expired'),
    re_path(r'^username_for_reset_password/$',views.username_for_reset_password,name='username_for_reset_password'),
    path('reset_password_page/<str:username>/<str:token>',views.reset_password_page,name='reset_password_page'),
    re_path(r'^reset_password/$',views.reset_password,name='reset_password'),
    re_path(r'^change_password/$',views.change_password,name='change_password'),
    
]