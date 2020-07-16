from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from listings.models import Listing
from .models import MailsToSend
# Create your views here.

def Home(requests):
	# for the listings to be only 4 
	listings = Listing.objects.filter()
	print(listings)
	if len(listings)<=2:
		context={'listings':listings}
	listings=listings[:4]
	if requests.POST:
		emailfield = requests.POST.get('newsletter')
		mailstosend = MailsToSend(email=emailfield)
		mailstosend.save()
	context={'listings' : listings}
	return render(requests, 'pages/home.html',context)

class AboutView(TemplateView):
	template_name = 'pages/about.html'
