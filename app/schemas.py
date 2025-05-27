from drf_yasg import openapi

# Talent registration schema
talent_register_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['full_name', 'email', 'role', 'password'],
    properties={
        'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='Full name of the talent'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the talent'),
        'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role of the talent (e.g., Frontend Developer)'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the talent'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the talent'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, description='Gender of the talent'),
        'country_of_residence': openapi.Schema(type=openapi.TYPE_STRING, description='Country of residence'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City of residence'),
        'profile_picture': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the talent’s profile picture'),
        'resume': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the talent’s resume file'),
        'cover_letter': openapi.Schema(type=openapi.TYPE_STRING, description='URL of the talent’s cover letter file'),
        'preferred_language': openapi.Schema(type=openapi.TYPE_STRING, description='Preferred language of the talent'),
        'website_or_portfolio': openapi.Schema(type=openapi.TYPE_STRING, description='Talent’s website or portfolio URL'),
        'social_links': openapi.Schema(type=openapi.TYPE_STRING, description='Social media links (e.g., LinkedIn, Twitter)'),
    }
)

# Employer registration schema
employer_register_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['full_name', 'email', 'password'],
    properties={
        'full_name': openapi.Schema(type=openapi.TYPE_STRING, description='Full name of the employer'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the employer'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the employer'),
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Phone number of the employer'),
        'company_name': openapi.Schema(type=openapi.TYPE_STRING, description='Name of the employer’s company'),
        'company_email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the employer’s company'),
        'business_challenges': openapi.Schema(type=openapi.TYPE_STRING, description='Challenges faced by the business'),
        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the company'),
        'funding_stage': openapi.Schema(type=openapi.TYPE_STRING, description='Company’s funding stage (e.g., Seed, Series A)'),
        'number_of_employees': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of employees in the company'),
    }
)

# OTP request schema
otp_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['email'],
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address to send the OTP to')
    }
)

# OTP verification schema
otp_verification_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['email', 'otp'],
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address used to request the OTP'),
        'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP code sent to the email'),
    }
)

# Signin schema
signin_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['email', 'password'],
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email address of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
    },
    example={
        'email': 'john@example.com',
        'password': 'password123',
    }
)

# Signin response schema
signin_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Refresh Token'),
        'access': openapi.Schema(type=openapi.TYPE_STRING, description='JWT Access Token'),
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
    },
    example={
        'refresh': 'some-refresh-token',
        'access': 'some-access-token',
        'message': 'Login successful',
    }
)
