from rest_framework import serializers
from app.models import User


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'full_name',
            'middle_name',
            'birth_day',
            'phone',
            'email',
        )