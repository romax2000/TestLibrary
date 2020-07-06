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
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.middle_name = validated_data.get('middle_name', instance.middle_name)
        instance.birth_day = validated_data.get('birth_day', instance.birth_day)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance