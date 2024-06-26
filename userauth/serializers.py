from rest_framework import serializers,status
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework.validators import ValidationError
from django.contrib.auth.hashers import make_password
from . models import User

class UserCreationSerializer(serializers.ModelSerializer):
     username=serializers.CharField(max_length=40,allow_blank=True)
     email=serializers.CharField(max_length=80,allow_blank=False)
     phone_number=PhoneNumberField(allow_null=False,allow_blank=False)
     password=serializers.CharField(allow_blank=False,write_only=True)

     class Meta:
        model=User
        fields=['id','username', 'email', 'phone_number','password']

     def validate(self,attrs):
        email_exists=User.objects.filter(username=attrs.get('email')).exists()

        if email_exists:
            raise ValidationError(detail="User with email exists",code=status.HTTP_403_FORBIDDEN)

        username_exists=User.objects.filter(username=attrs.get('username')).exists()

        if username_exists:
            raise ValidationError(detail="User with username exists",code=status.HTTP_403_FORBIDDEN)

        phonenumber_exists=User.objects.filter(username=attrs.get('phone_number')).exists()

        if phonenumber_exists:
            raise ValidationError(detail="User with phonenumber",code=status.HTTP_403_FORBIDDEN)
        return super().validate(attrs)

     def create(self,validated_data):
        new_user=User(**validated_data)

        new_user.password=make_password(validated_data.get('password'))

        new_user.save()

        return new_user
    


