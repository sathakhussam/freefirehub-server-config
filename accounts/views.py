from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as login_dj, logout
from .models import MyUser,BaseUserManager
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from listings.models import Listing, Sale
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import registration,loginform
from .admin import UserCreationForm
# email configurations
from django.core.mail import send_mail
from django.conf import settings
from random import randint
# Create your views here.



def login(requests):
	form = loginform()
	if requests.method == 'POST':
		form = loginform(requests.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user != None:
				login_dj(requests, user)
				return redirect('dashboard')
	return render(requests, 'accounts/login.html', {'form':form})

def register(requests):
	form = registration()
	if requests.method == 'POST':
		form = registration(requests.POST)
		if MyUser.objects.filter(email=requests.POST.get('email')).count():
			context ={'form':form, 'error': 'Email already exists'}
			return render(requests, 'accounts/register.html',context)
		elif MyUser.objects.filter(username=requests.POST.get('username')).count():
			context ={'form':form, 'error': 'Username already exists'}
			return render(requests, 'accounts/register.html',context)
		elif MyUser.objects.filter(phone=requests.POST.get('phone')).count():
			context ={'form':form, 'error': 'Phone already exists'}
			return render(requests, 'accounts/register.html',context)
		elif requests.POST.get('password')!=requests.POST.get('password_confirm'):
			context ={'form':form, 'error': "Password doesn't match"}
			return render(requests, 'accounts/register.html',context)
		
		if form.is_valid():
			print(MyUser.objects.filter(email=form.cleaned_data['email']))
			requests.session['register_form_cookie_username'] = form.cleaned_data['username']
			requests.session['register_form_cookie_email'] = form.cleaned_data['email']
			requests.session['register_form_cookie_phone'] = form.cleaned_data['phone']
			requests.session['register_form_cookie_password'] = form.cleaned_data['password']
			return redirect(verify_email)
	context = {'form':form}
	return render(requests, 'accounts/register.html',context)

def verify_email(requests):

	if requests.session['register_form_cookie_email'] and requests.session['register_form_cookie_phone'] and requests.session['register_form_cookie_username'] and requests.session['register_form_cookie_password']:
		if 'otp_num' in requests.session:
			print(requests.session['otp_num'])
			if requests.method == 'POST':
				print(requests.session['otp_num'])
				# print(requests.POST.get('otp_field')==intrequests.session['otp_num'])
				if int(requests.POST.get('otp_field'))==requests.session['otp_num']:
					form = MyUser(email=requests.session['register_form_cookie_email'],username=requests.session['register_form_cookie_username'],phone=requests.session['register_form_cookie_phone'])
					form.set_password(requests.session['register_form_cookie_password'])
					form.save()
					del requests.session['otp_num']
					del requests.session['register_form_cookie_username']
					del requests.session['register_form_cookie_email']
					del requests.session['register_form_cookie_phone']
					del requests.session['register_form_cookie_password']
					return redirect(login)
				else:
					return render(requests, 'accounts/verify.html',{'otp_num':requests.session['otp_num'], 'error':'The otp is incorrect'})
			return render(requests, 'accounts/verify.html',{'otp_num':requests.session['otp_num'], 'email': requests.session['register_form_cookie_email']})

			
		subject = 'Thank you for registering to our website'
		otp_num = randint(10000,99999)
		message = f"Here's your otp : {otp_num}"
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [requests.session['register_form_cookie_email'],]
		# 'mohammedmufeeth1301@gmail.com'
		send_mail( subject, message, email_from, recipient_list )
		subject = 'Someone is registering and in otp process'
		message = f"Here's {otp_num} the otp of them."
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ['sathakhussam@gmail.com',]
		# 'mohammedmufeeth1301@gmail.com'
		send_mail( subject, message, email_from, recipient_list )
		requests.session['otp_num'] = otp_num
		if requests.method == 'POST':
			if int(requests.POST.get('otp_field'))==requests.session['otp_num']:
				requests.session['register_form_cookie'].save()
				del requests.session['otp_num']
				return redirect(login)
			else:
				return render(requests, 'accounts/verify.html',{'otp_num':requests.session['otp_num'], 'error':'The otp is incorrect'})
		return render(requests, 'accounts/verify.html',{'otp_num':requests.session['otp_num'], 'email': requests.session['register_form_cookie_email']})
	else:
		redirect(register)
def resend_otp(requests):
	del requests.session['otp_num']
	return redirect(verify_email)

@login_required	
def dashboard(requests):
	listings_userS = Listing.objects.filter(seller_user=requests.user)
	sales = Sale.objects.filter(customer_user=requests.user)
	lists=[]
	for sale in sales:
		obj = get_object_or_404(Listing,username=sale.ListingAcc.username)
		lists.append(obj.id)
	context = {
		'listings': listings_userS,
		'sales':sales,
		'lists':lists
	}
	return render(requests, 'accounts/dashboard.html', context)
@login_required
def Mylogout(requests):
	logout(requests)
	retu

	
# I still have to make some changes to it and also add the logout view which redirects