from django import forms
from blog.models import post
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name': forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
        
        }


class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label='Password',strip=False ,widget=forms.PasswordInput(attrs={'autocomplete':True,'class':'form-control'}))


# model form
class Postform(forms.ModelForm):
    class Meta:
        model=post

        fields=['title','desc']
        labels={'title':'Title','desc':'Description'}
        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),'desc':forms.Textarea(attrs={'class':'form-control'})}



