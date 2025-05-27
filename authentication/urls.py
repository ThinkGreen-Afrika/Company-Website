from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.shortcuts import render
from django.urls import path, include
from django.contrib import admin
from app import views
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Swagger setup for API documentation
schema_view = get_schema_view(
   openapi.Info(
      title="ThinkGreen Afrika API",
      default_version='v1',
      description="API documentation for ThinkGreen Afrika",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="your-email@example.com"),
      license=openapi.License(name="BSD License"),
   ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
)

# This view function will render the 'index.html'
def homepage(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', homepage, name='homepage'),  # Homepage
    path('select/', views.select_view, name='select'),
    path('podcast/', views.podcast_view, name='podcast'),
    path('book/', views.book_view, name='book'),
    path('home/', views.home_view, name='home'),
    path('talent/', views.talent_view, name='talent'),
    path('employer/', views.employer_view, name='employer'),
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),

    # Swagger documentation URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.yaml', schema_view.without_ui(cache_timeout=0), name='schema-json'),

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

    # Include the app's other URLs
    path('api/', include('app.urls')),  # Include other app-specific URLs if necessary
]

if settings.DEBUG:  # Only serve media in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)