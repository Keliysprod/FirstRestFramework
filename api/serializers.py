from rest_framework import serializers
from api.models import CustomUser,Event,Invited

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields = (
            '__all__'
        )


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields = (
            '__all__'
        )

class InvitedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Invited
        fields = (
            '__all__'
        )