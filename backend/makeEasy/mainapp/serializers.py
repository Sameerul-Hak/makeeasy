from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Register
        fields=['name','phone','email','password','conform_password']
    

    