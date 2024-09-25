from rest_framework import serializers

from core.abstract.serializers import AbstractSerializer
from core.user.models import User

class UserSerializer(AbstractSerializer):
 
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "first_name",
            "last_name",
            "email",
            "is_active",
            'is_superuser',
            "created",
            "updated",
        ]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]