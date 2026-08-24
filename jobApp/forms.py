from django import forms
from jobApp.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegiForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username','user_types','email','password1','password2']


        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        for i in self.fields:
            self.fields[i].widget.attrs.update({
                'class' : 'form-control'
        })


class LoginForm(AuthenticationForm):
    pass 



class RecForm(forms.ModelForm):
    class Meta:
        model = RecProfile
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    
            for i in self.fields:
                self.fields[i].widget.attrs.update({
                    'class' : 'form-control'
            })

class JobSeekerForm(forms.ModelForm):
    class Meta:
        model = JobSeekerProfile 
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
    
    
            for i in self.fields:
                self.fields[i].widget.attrs.update({
                    'class' : 'form-control'
            })