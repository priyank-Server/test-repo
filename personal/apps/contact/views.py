from apps.contact import models, serializers

from rest_framework import generics


class ContactView(generics.CreateAPIView):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer

