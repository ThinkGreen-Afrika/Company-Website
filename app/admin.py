from django.contrib import admin
from .models import Talent, Employer  # Import your models
from django.utils.html import format_html
# Register Talent model in Django admin
@admin.register(Talent)
class TalentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'profile_picture_display', 'resume_link', 'cover_letter_link')

    def profile_picture_display(self, obj):
        if obj.profile_picture:
            return format_html('<img src="{}" width="50" height="50" />', obj.profile_picture.url)
        return 'No picture'

    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}">Download Resume</a>', obj.resume.url)
        return 'No resume'

    def cover_letter_link(self, obj):
        if obj.cover_letter:
            return format_html('<a href="{}">Download Cover Letter</a>', obj.cover_letter.url)
        return 'No cover letter'

# Register Employer model in Django admin
@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 
        'company_name', 
        # 'company_email',
        'phone_number', 
        'location', 
        'funding_stage', 
        'number_of_employees'
    )
    search_fields = ('full_name', 'company_name', 'phone_number')
    list_filter = ('funding_stage', 'location')




# Register your models here.
