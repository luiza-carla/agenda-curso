from django import forms
from contact.models import Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation


class ContactForm(forms.ModelForm):

    picture = forms.ImageField(widget=forms.FileInput(attrs={'accept': 'image/*', }), required=False)
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category', 'picture',
            )

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email',
            ValidationError('Email já existe', code='email_exists'))
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(required=False)
    password2 = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user

    def clean(self):
        super().clean()
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error('password2', ValidationError('Senhas não conferem', code='password_mismatch'))
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error('email',
                ValidationError('Email já existe', code='email_exists'))
            return email
        
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except forms.ValidationError as error:
                self.add_error('password1', error)
        return password1