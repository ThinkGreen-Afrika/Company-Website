from django.urls import path
from . import views
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static


# This view function will render the 'index.html'
def homepage(request):
    return render(request, 'index.html')

urlpatterns = [
    path('', homepage, name='homepage'),  # Homepage
    path('select/', views.select_view, name='select'),
    path('podcast/', views.podcast_view, name='podcast'),
    path('book/', views.book_view, name='book'),
    path('home/', views.home_view, name='home'),
    path('about_us/', views.about_view, name='about_us'),
    path('program/', views.program_view, name='program'),
    path('solutions/', views.solutions_view, name='solutions'),
    path('tvetproject/', views.tvetproject_view, name='tvetproject'),
    path('talent/', views.talent_view, name='talent'),
    path('employer/', views.employer_view, name='employer'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),




    # Employer URLs
    path('signup/employer/', views.signup_employer, name='signup_employer'),
    # path('verify-email/employer/<str:username>/', views.verify_token_employer, name='verify_token_employer'),
    # path('signin/employer/', views.signin_employer, name='login_employer'),

    # Talent URLs
    path('signup/talent/', views.signup_talent, name='signup_talent'),
    # path('verify-email/talent/<str:username>/', views.verify_token_talent, name='verify_token_talent'),
    # path('signin/talent/', views.signin_talent, name='login_talent'), #View to render login page

    path('logout/', views.logout_view, name='logout'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe'),

    
    # # OTP-related routes
    # path('otp/request', views.request_otp, name='request_otp'),
    # path('otp/verify', views.verify_otp, name='verify_otp'),
    # path('otp/resend', views.resend_otp, name='resend_otp'),
    
    # # Signin route
    # path('signin', views.signin, name='signin'),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:  # Only serve media in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)