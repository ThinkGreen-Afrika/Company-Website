from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import OtpToken
from django.core.mail import send_mail
from django.utils import timezone

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance, created, **kwargs):
    if created:
        # Skip OTP creation for superusers
        if instance.is_superuser:
            return
        
        # Create OTP token and deactivate the user until verification
        otp = OtpToken.objects.create(user=instance, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
        instance.is_active = False
        instance.save()

        # Email credentials
        subject = "Email Verification"
        message = f"""
            Hi {instance.username}, here is your OTP: {otp.otp_code}
            It expires in 5 minutes. Use the link below to verify your email:
            http://127.0.0.1:8000/verify-email/{instance.username}
        """
        sender = "clintonmatics@gmail.com"
        receiver = [instance.email]

        # Send email
        send_mail(
            subject,
            message,
            sender,
            receiver,
            fail_silently=False,
        )
