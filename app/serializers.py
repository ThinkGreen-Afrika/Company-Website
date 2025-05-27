from rest_framework import serializers
from .models import Talent, Employer

# Serializer for Talent model
class TalentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talent
        fields = '__all__'


# Serializer for Employer model
class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'
