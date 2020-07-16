from django import forms
from accounts.models import MyUser
class registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta():
        model = MyUser
        fields = ['email', 'username', 'phone']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'phone': forms.NumberInput(attrs={'placeholder': 'Phone'}),
        }
    def check_pass(self):
        if self.cleaned_data["password"]!=self.cleaned_data["password"]:
            raise forms.ValidationError('Both Passwords must match!')
        return self.password
    
    def save(self, commit=True):
    # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)