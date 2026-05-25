from django import forms
from app.models import SignupModel


class SignupForm(forms.ModelForm):
    # name = forms.CharField(error_messages={'required':"Name is required"}, label="Name :",max_length=50,min_length=1,required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    # username  = forms.CharField(error_messages={'required':"Username is required"}, label="Username :",required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    # email = forms.EmailField(error_messages = {'required':"Email is required"},label="Email :", max_length=50, min_length=1, required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    # password = forms.CharField(error_messages = {'required':"password is required"},label="Password :", max_length=50, min_length=8, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = SignupModel
        fields = '__all__'
        labels = {'name': 'Enter Name'}
        error_messages = {'name': {'required': 'Email is required'}}
        widgets = {
            'name': forms.TextInput(attrs={
                'style': 'padding:10px 12px; border:1px solid #e2e2e2; border-radius:8px; font-size:14px; outline:none;'
            }),
            'username': forms.TextInput(attrs={
                'style': 'padding:10px 12px; border:1px solid #e2e2e2; border-radius:8px; font-size:14px; outline:none;'
            }),
            'email': forms.EmailInput(attrs={
                'style': 'padding:10px 12px; border:1px solid #e2e2e2; border-radius:8px; font-size:14px; outline:none;'
            }),
            'password': forms.PasswordInput(attrs={
                'style': 'padding:10px 12px; border:1px solid #e2e2e2; border-radius:8px; font-size:14px; outline:none;'
            }),
        }


# Or use fields = '__all__' to include all model fields
# Or use exclude = ['field_to_exclude'] to exclude specific fields


class loginForm(forms.Form):
    email = forms.EmailField(label="Email :", required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password :", required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="Age :", required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_super = forms.BooleanField(
        label = "Super", 
        required=True, 
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="Check this box if you are a super user.",
        error_messages={'required': "You must confirm that you are a super user."})