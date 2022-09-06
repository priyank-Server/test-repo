from rest_framework import serializers
from apps.contact import models


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = '__all__'
