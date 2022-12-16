from rest_framework import serializers

from .models import Information

class InformationSerializr(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'