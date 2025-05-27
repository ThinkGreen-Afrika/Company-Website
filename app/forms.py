from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import NewsletterSubscriber
from django.contrib.auth import get_user_model
from .models import Employer, Talent

# User form (common registration form for all users)
class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email address", "class": "form-control"}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter full name", "class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"}))
    
    class Meta:
        model = get_user_model()
        fields = ["email", "full_name", "password1", "password2"]

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['full_name']
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# Employer form (additional fields specific to employers)
class EmployerRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter full name", "class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter phone number", "class": "form-control"}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter company name (optional)", "class": "form-control"}), required=False)
    company_email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter company email (optional)", "class": "form-control"}), required=False)
    business_challenges = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "List of business challenges (optional)", "class": "form-control"}), required=False)
    location = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your location (optional)", "class": "form-control"}), required=False)
    funding_stage = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Current funding stage (optional)", "class": "form-control"}), required=False)
    number_of_employees = forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder": "Number of employees (optional)", "class": "form-control"}), required=False)

    class Meta:
        model = Employer
        fields = ['full_name', 'phone_number', 'company_name', 'company_email', 'business_challenges', 'location', 'funding_stage', 'number_of_employees']

# Talent form (additional fields specific to talents)
class TalentRegistrationForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter full name", "class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter phone number", "class": "form-control"}))
    role = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter your role (e.g., frontend developer, designer)", "class": "form-control"}))
    gender = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter gender", "class": "form-control"}))
    country_of_residence = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter country of residence (optional)", "class": "form-control"}), required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter city (optional)", "class": "form-control"}), required=False)
    profile_picture = forms.ImageField(required=False)
    resume = forms.FileField(required=False)
    cover_letter = forms.FileField(required=False)
    preferred_language = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter preferred language", "class": "form-control"}))
    website_or_portfolio = forms.URLField(widget=forms.URLInput(attrs={"placeholder": "Enter website or portfolio URL (optional)", "class": "form-control"}), required=False)
    social_links = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter social links (optional)", "class": "form-control"}), required=False)

    class Meta:
        model = Talent
        fields = ['full_name', 'phone_number', 'role', 'gender', 'country_of_residence', 'city', 'profile_picture', 'resume', 'cover_letter', 'preferred_language', 'website_or_portfolio', 'social_links']

class NewsletterSubscriptionForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter first name", "class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter last name", "class": "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder": "Enter email address", "class": "form-control"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter phone number", "class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Enter message (optional)", "class": "form-control"}), required=False)
    class Meta:
        model = NewsletterSubscriber
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'message']
