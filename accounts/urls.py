from django.contrib.auth import views as auth_views
# from django.core.urlresolvers import reverse_lazy
from django.urls import path
from . import views

urlpatterns = [
	path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('logout/', auth_views.logout_then_login, name='logout'),
	path('verify/', views.verify_email, name='verify_email'),
	path('resend/', views.resend_otp, name='resend_otp'),
]


# url(r'^logout/$', 
     
#     {'next_page': reverse_lazy('cost_control_app:login')},
#     name='logout',
# )