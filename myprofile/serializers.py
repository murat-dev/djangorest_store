from rest_framework import serializers

from myprofile.models import ProfileCustomer


class ProfileCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCustomer
        fields = '__all__'
