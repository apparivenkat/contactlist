from rest_framework.serializers import ModelSerializer
from .models import Contact



class ContactSerializer(ModelSerializer):

    class Meta:
        model = Contact
        fields = ['id', 'coutry', 'first_name', 'last_name', 'phone_no', 'contact_picture', 'is_favourite']