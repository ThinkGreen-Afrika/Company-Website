from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid

class Talent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    talent_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)  # e.g., frontend developer, designer
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=10)
    country_of_residence = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/')
    preferred_language = models.CharField(max_length=50)
    website_or_portfolio = models.URLField(blank=True, null=True)
    social_links = models.CharField(max_length=255)
    otp = models.CharField(max_length=6, blank=True, null=True)  # Add field to store OTP

    def __str__(self):
        return self.full_name


class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employer_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_email= models.EmailField(blank=True, null=True)
    business_challenges = models.TextField(blank=True, null=True)  # Optional field for describing challenges
    location = models.CharField(max_length=255, blank=True, null=True)
    funding_stage = models.CharField(max_length=100, blank=True, null=True)  # E.g., Seed, Series A, etc.
    number_of_employees = models.IntegerField(blank=True, null=True)  # Optional field for employees count
    otp = models.CharField(max_length=6, blank=True, null=True)  # Add field to store OTP

    def __str__(self):
        return self.full_name


# Function to calculate OTP expiration time
def get_expiry_time():
    return timezone.now() + timezone.timedelta(minutes=10)

# OTP Model for verification
class OtpToken(models.Model):
    email = models.CharField(max_length=225)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField(default=False)
    expires_at = models.DateTimeField(default=get_expiry_time)

    def __str__(self):
        return f'OTP for {self.email}'
    
# Newsletter subscriber model

class NewsletterSubscriber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


# Create your models here.
