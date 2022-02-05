from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
UserModel=get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields='__all__'
        extra_kwargs = {"password": {"write_only": True}}

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

    def validate(self, attrs):
        if attrs.get('username'):
            if not (attrs['username'].isalnum()):
                raise ValidationError('Enter a valid username')
        if attrs.get('firstname'):
            if not ((attrs['firstname'].isalpha())):
                raise ValidationError('Enter Valid FirstName')
        if attrs.get('mobile'):
            if ((len(attrs['mobile']) < 10) and (attrs['mobile'].isnumeric())):
                raise ValidationError('Enter Valid Mobile')
        if attrs.get('email'):
            if not "@" in attrs['email'] or not (".com" or ".org" or ".edu" or ".gov" or ".net") in attrs['email'][-4:]:
                raise ValidationError('Invalid Email')

        return attrs