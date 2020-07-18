from django import forms
from listings.models import Listing,PaymentsStore
class create_listing(forms.ModelForm):
    class Meta():
        model = Listing
        fields = ['freefire_id','username','level', 'description', 'estimated_price','signed_up_with', 'account_email','account_password','photo_main','video_main']
        widget = {
            'video_main': forms.FileInput(attrs={'accept': 'video/*'}),
            'photo_main': forms.FileInput(attrs={'class':'sample','accept': 'image/*'})
            'freefire_id': forms.NumberInput(attrs={})
        }
class paymentsabout(forms.ModelForm):
    class Meta():
        model = PaymentsStore
        fields = ['phone_num', 'order_id', 'price']