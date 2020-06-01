from rest_framework import serializers
from .models import Signup

class SignUpSerializer(serializers.ModelSerializer):
    passangers_id = serializers.CharField(required=False)
    name = serializers.CharField(required=False)
    phone = serializers.IntegerField(required=False)
    email_id = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    class Meta:
        model = Signup
        fields ='__all__'




