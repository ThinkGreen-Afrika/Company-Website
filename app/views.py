import logging

# Get an instance of a logger

logger = logging.getLogger(__name__)

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import EmailMessage
import json
import PIL
import random
from django.conf import settings
from rest_framework import status
from django.contrib.auth import logout
from rest_framework import status
from django.utils import timezone
from rest_framework.response import Response
from .models import Talent, Employer, OtpToken, NewsletterSubscriber
from .schemas import (
    talent_register_schema,
    employer_register_schema,
    otp_request_schema,
    otp_verification_schema,
    signin_schema,
    signin_response_schema
)
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmployerRegistrationForm, TalentRegistrationForm, UserRegistrationForm, NewsletterSubscriptionForm
from django.contrib import messages
from .models import OtpToken
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError



# View to handle the employer selection page
def select_view(request):
    return render(request, 'select.html')

def podcast_view(request):
    return render(request, 'podcast.html')

def talent_view(request):
    return render(request, 'talent.html')

def employer_view(request):
    return render(request, 'employer.html')


# Additional Pages (Redesigns)
def program_view(request):
    return render(request, 'program.html')

def solutions_view(request):
    return render(request, 'solutions.html')  

def tvetproject_view(request):
    return render(request, 'tvetproject.html')

def about_view(request):
    return render(request, 'about_us.html')  



def book_view(request):
    # try:
    return render(request, 'book.html')
    # except Exception as e:
    #     logger.error(f"Error in book_view: {str(e)}")
    #     return HttpResponse("An error occurred. Please try again later.", status=500)

def home_view(request):
    return render(request, 'index.html')

def employer_dashboard(request):
    return render(request, 'employer_dashboard.html')

# Employer Signup View
def signup_employer(request):
    user_form = UserRegistrationForm()  # Ensure this is defined at the top, outside try-except
    employer_form = EmployerRegistrationForm()

    try:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            employer_form = EmployerRegistrationForm(request.POST)

            # Log the incoming request data
            logger.info("Form Submission Received - POST Data:")
            logger.info(request.POST)

            if user_form.is_valid() and employer_form.is_valid():
                # Get email from the form
                email = user_form.cleaned_data.get('email')

                # Check if user already exists
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'status': 'exists', 'message': 'You have already registered with this email address.'})
                    # return redirect('home')

                user = user_form.save(commit=False)
                user.is_active = True  # Set user as active directly since we're not using OTP in this flow
                user.username = employer_form.cleaned_data.get('full_name')  # Set username as full name
                user.save()

                # Create Employer instance linked to user
                employer = employer_form.save(commit=False)
                employer.user = user
                employer.save()

                # Extract additional employer details from the form
                phone_number = employer_form.cleaned_data.get('phone_number')
                company_name = employer_form.cleaned_data.get('company_name')
                company_email = employer_form.cleaned_data.get('company_email')
                business_challenges = employer_form.cleaned_data.get('business_challenges')
                location = employer_form.cleaned_data.get('location')
                funding_stage = employer_form.cleaned_data.get('funding_stage')
                number_of_employees = employer_form.cleaned_data.get('number_of_employees')

                # Send Thank You message to Employer
                subject_employer = "Thank You for Registering - ThinkGreen Afrika"
                message_employer = f"Hi {user.username},\n\nThank you for registering with ThinkGreen Afrika! We are excited to have you on board. Our team will get back to you within three working days.\n\n"
                sender = "amtwagirayezu@gmail.com"  # Replace with your email
                receiver_employer = [user.email, company_email]
                send_mail(subject_employer, message_employer, sender, receiver_employer, fail_silently=False)

                # Send email to ThinkGreen Afrika with additional details
                subject = "New Employer Registered - ThinkGreen Afrika"
                message = (
                    f"Employer {user.username} has registered.\n\nDetails:\n"
                    f"Name: {user.username}\n"
                    f"Email: {user.email}\n"
                    f"Phone Number: {phone_number}\n"
                    f"Company Name: {company_name}\n"
                    f"Company Email: {company_email}\n"
                    f"List of Business Challenges: {business_challenges}\n"
                    f"Location: {location}\n"
                    f"Current Funding Stage: {funding_stage}\n"
                    f"Number of Employees: {number_of_employees}\n"
                )
                receiver = ["thinkgreenafrika.org@gmail.com"]  # Replace with ThinkGreen Afrika's email


                email_message = EmailMessage(subject, message, sender, receiver)
                email_message.send(fail_silently=False)

                # Redirect to homepage
                messages.success(request, "Account created successfully! Thank you for registering.")
                return redirect('home')
            else:
                # Log errors if forms are not valid
                logger.error("User form errors: %s", user_form.errors)
                logger.error("Employer form errors: %s", employer_form.errors)
                messages.error(request, "There was an error with the submission. Please correct the errors and try again.")

    except IntegrityError as e:
        logger.error(f"Database IntegrityError in signup_employer view: {str(e)}")
        messages.error(request, "An account with this information already exists. Please try logging in.")

    except Exception as e:
        logger.error(f"Unexpected error in signup_employer view: {str(e)}")
        messages.error(request, "An unexpected error occurred. Please try again later.")

    context = {"user_form": user_form, "employer_form": employer_form}
    return render(request, "signup_employer.html", context)


# # Employer Email Verification View
# def verify_token_employer(request, username):
#     user = get_object_or_404(User, username=username)
#     user_otp = OtpToken.objects.filter(email=user.email).last()

#     if request.method == 'POST':
#         otp_code = request.POST.get('otp_code')  # Combined OTP from hidden field
#         if otp_code and user_otp and user_otp.otp == otp_code:
#             if user_otp.expires_at > timezone.now():
#                 user.is_active = True
#                 user.save()
#                 messages.success(request, "Account activated successfully! You can now log in.")
#                 return redirect("login_employer")
#             else:
#                 messages.warning(request, "The OTP has expired, please request a new OTP.")
#                 return redirect("verify_token_employer", username=user.username)
#         else:
#             messages.warning(request, "Invalid OTP entered, please try again.")
#             return redirect("verify_token_employer", username=user.username)

#     context = {'user': user}
#     return render(request, "otp_c.html", context)



# # Employer Sign-in View
# def signin_employer(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         try:
#             username = User.objects.get(email=email).username
#         except User.DoesNotExist:
#             messages.warning(request, "Invalid email or password.")
#             return redirect("login_employer")
        
#         user = authenticate(request, username=username, password=password)

#         if user is not None and user.is_active:
#             login(request, user)
#             messages.success(request, f"Hi {request.user.username}, you are now logged in.")
#             return redirect("employer_dashboard")  # Change to your employer dashboard URL
#         else:
#             messages.warning(request, "Invalid credentials or account is not active.")
#             return redirect("login_employer")

#     return render(request, "login_employer.html", {"form": None})


### TALENT REGISTRATION, OTP VERIFICATION, AND SIGN-IN VIEWS ###

# Talent Signup View
def signup_talent(request):
    user_form = UserRegistrationForm()  # Ensure this is defined at the top, outside try-except
    talent_form = TalentRegistrationForm()

    try:
        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST)
            talent_form = TalentRegistrationForm(request.POST, request.FILES)

            # Log the incoming request data
            logger.info("Form Submission Received - POST Data:")
            logger.info(request.POST)
            logger.info(request.FILES)

            if user_form.is_valid() and talent_form.is_valid():
                # Get email from the form
                email = user_form.cleaned_data.get('email')

                # Check if user already exists
                if User.objects.filter(email=email).exists():
                    return JsonResponse({'status': 'exists', 'message': 'You have already registered with this email address.'})

                user = user_form.save(commit=False)
                user.is_active = True  # Set user as active directly since we're not using OTP in this flow
                user.username = talent_form.cleaned_data.get('full_name')  # Set username as full name
                user.save()


                # Create Talent instance linked to user
                talent = talent_form.save(commit=False)
                talent.user = user
                talent.save()

                # Send Thank You message to Talent
                subject_talent = "Thank You for Registering - ThinkGreen Afrika"
                message_talent = f"Hi {user.username},\n\nThank you for registering with ThinkGreen Afrika! We are excited to have you on board."
                sender = "amtwagirayezu@gmail.com"  # Replace with your email
                receiver_talent = [user.email]
                send_mail(subject_talent, message_talent, sender, receiver_talent, fail_silently=False)

                # Send email to ThinkGreen Afrika
                subject = "New Talent Registered - ThinkGreen Afrika"
                message = f"Talent {user.username} has registered.\n\nDetails:\nName: {user.username}\nEmail: {user.email}\n"
                receiver = ["thinkgreenafrika.org@gmail.com"]  # Replace with ThinkGreen Afrika's email

                email = EmailMessage(subject, message, sender, receiver)

                # Attach the resume, cover letter, and profile picture if available
                if 'resume' in request.FILES:
                    resume = request.FILES['resume']
                    resume.open('rb')  # Open the file in binary mode
                    email.attach(resume.name, resume.read(), resume.content_type)

                if 'cover_letter' in request.FILES:
                    cover_letter = request.FILES['cover_letter']
                    cover_letter.open('rb')  # Open the file in binary mode
                    email.attach(cover_letter.name, cover_letter.read(), cover_letter.content_type)

                if 'profile_picture' in request.FILES:
                    profile_picture = request.FILES['profile_picture']
                    profile_picture.open('rb')  # Open the file in binary mode
                    email.attach(profile_picture.name, profile_picture.read(), profile_picture.content_type)
                email.send(fail_silently=False)

                # Redirect to homepage
                return redirect('home')
            else:
                # Log errors if forms are not valid
                logger.error("User form errors: %s", user_form.errors)
                logger.error("Talent form errors: %s", talent_form.errors)
                messages.error(request, "There was an error with the submission. Please correct the errors and try again.")

    except Exception as e:
        logger.error(f"Unexpected error in signup_talent view: {str(e)}")
        messages.error(request, "An unexpected error occurred. Please try again later.")

    context = {"user_form": user_form, "talent_form": talent_form}
    return render(request, "signup_talent.html", context)

# Logout View
def logout_view(request):
    try:
        # Log out the current user
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        # Redirect to the homepage or login page after logout
        return redirect('home_view')  # Assuming you have a home view
    except Exception as e:
        logger.error(f"Error occurred during logout: {str(e)}")
        messages.error(request, "An error occurred during logout. Please try again later.")
        return redirect('home_view')
        

# Newsletter Subscription View
def subscribe_newsletter(request):
    form = NewsletterSubscriptionForm()

    try:
        if request.method == 'POST':
            form = NewsletterSubscriptionForm(request.POST)

            # Log the incoming request data
            logger.info("Newsletter Subscription Form Submission Received - POST Data:")
            logger.info(request.POST)

            if form.is_valid():
                # Check if the user has already subscribed
                email = form.cleaned_data.get('email')
                if NewsletterSubscriber.objects.filter(email=email).exists():
                    # messages.info(request, "You have already subscribed to our newsletter.")
                    return render(request, "newsletter.html", {"form": form, "already_subscribed": True})  
                
                # Save the subscriber's email
                subscriber = form.save()
                # messages.success(request, "Thank you for subscribing to our newsletter!")

                # Send Thank You message to Subscriber
                subject_user = "Thank You for Subscribing to ThinkGreen Newsletter"
                message_user = (
                    f"Hi {subscriber.email},\n\nThank you for subscribing to the ThinkGreen newsletter! "
                    "Stay tuned for updates. You'll be the first to hear about our latest news and opportunities."
                )
                sender = "amtwagirayezu@gmail.com"  # Replace with your email
                receiver_user = [subscriber.email]

                # Send email to ThinkGreen Afrika
                subject_company = "New Newsletter Subscription"
                message_company = (
                    f"A new user has subscribed to the newsletter.\n\nDetails:\nEmail: {subscriber.email}"
                )
                receiver_company = ["thinkgreenafrika.org@gmail.com"]  # Replace with ThinkGreen Afrika's email

                # Send both emails
                email_sent_user = send_mail(subject_user, message_user, sender, receiver_user, fail_silently=False)
                email_to_company = EmailMessage(subject_company, message_company, sender, receiver_company)
                email_sent_company = email_to_company.send(fail_silently=False)

                # Check if both emails were sent successfully
                if email_sent_user and email_sent_company:
                    logger.info(f"Emails sent successfully for subscription by {subscriber.email}")
                    messages.success(request, "Thank you for subscribing to our newsletter!")
                else:
                    logger.warning(f"Emails could not be sent for subscription by {subscriber.email}")
                    messages.warning(request, "There was an issue sending confirmation emails, but you are subscribed.")

                # Redirect to homepage after all emails are sent
                return redirect('home')

            else:
                # Log errors if forms are not valid
                logger.error("Newsletter Subscription Form errors: %s", form.errors)
                messages.error(request, "There was an error with your subscription. Please try again.")

    except Exception as e:
        logger.error(f"Unexpected error in subscribe_newsletter view: {str(e)}")
        messages.error(request, "An unexpected error occurred. Please try again later.")

    context = {"form": form}
    return render(request, "newsletter.html", context)