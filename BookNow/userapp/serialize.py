from rest_framework import serializers
from .models import UserModel
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def validate(self, data):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password', '')

        if not name:
            raise serializers.ValidationError({
                'errorCode': '2000',
                'message': 'Name should not empty'
            })

        if any(char in "!@#$%^&*()-+" for char in name):
            raise serializers.ValidationError({
                'errorCode': '2001',
                'message': 'Name should not contain any special character'
            })
        if any(char.isdigit() for char in name):
            raise serializers.ValidationError({
                'errorCode': '2002',
                'message': 'Name Should not Contain Any Number'
            })
        if not email:
            raise serializers.ValidationError({
                'errorCode': '3000', 'message': 'Email Should not be Empty'
            })
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError({
                'errorCode': '3001',
                'message': 'Email is not valid'
            })

        if not password:
            raise serializers.ValidationError({
                'errorCode': '1000',
                'message': 'Password should not be empty'
            })

        if len(password) < 4:
            raise serializers.ValidationError({
                'errorCode': '1001',
                'message': 'Password should be at least 4 characters long'
            })

        if len(password) > 8:
            raise serializers.ValidationError({
                'errorCode': '1002',
                'message': 'Password should be at most 8 characters long'
            })

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1003',
                'message': 'Password should contain at least one uppercase letter'
            })

        if not any(char.islower() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1004',
                'message': 'Password should contain at least one lowercase letter'
            })

        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1005',
                'message': 'Password should contain at least one number'
            })

        if not any(char in "!@#$%^&*()-+" for char in password):
            raise serializers.ValidationError({
                'errorCode': '1006',
                'message': 'Password should contain at least one special character'
            })

        if ' ' in password:
            raise serializers.ValidationError({
                'errorCode': '1007',
                'message': 'Password should not contain white spaces'
            })

        return data


class LoginSerialize(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"

    def validate(self, data):
        name = data.get('name')
        email = data.get('email')
        password = data.get('password', '')

        if not email:
            raise serializers.ValidationError({
                'errorCode': '3000', 'message': 'Email Should not be Empty'
            })
        try:
            validate_email(email)
        except ValidationError:
            raise serializers.ValidationError({
                'errorCode': '3001',
                'message': 'Email is not valid'
            })

        if not password:
            raise serializers.ValidationError({
                'errorCode': '1000',
                'message': 'Password should not be empty'
            })

        if len(password) < 4:
            raise serializers.ValidationError({
                'errorCode': '1001',
                'message': 'Password should be at least 4 characters long'
            })

        if len(password) > 8:
            raise serializers.ValidationError({
                'errorCode': '1002',
                'message': 'Password should be at most 8 characters long'
            })

        if not any(char.isupper() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1003',
                'message': 'Password should contain at least one uppercase letter'
            })

        if not any(char.islower() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1004',
                'message': 'Password should contain at least one lowercase letter'
            })

        if not any(char.isdigit() for char in password):
            raise serializers.ValidationError({
                'errorCode': '1005',
                'message': 'Password should contain at least one number'
            })

        if not any(char in "!@#$%^&*()-+" for char in password):
            raise serializers.ValidationError({
                'errorCode': '1006',
                'message': 'Password should contain at least one special character'
            })

        if ' ' in password:
            raise serializers.ValidationError({
                'errorCode': '1007',
                'message': 'Password should not contain white spaces'
            })

        return data
