from rest_framework import serializers

from Admin.models import Admin


# from .model import Admin
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=Admin
        fields = "__all__"

