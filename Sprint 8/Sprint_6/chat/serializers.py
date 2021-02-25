from rest_framework import serializers
from chat.models import chatnombres


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = chatnombres
        fields = "__all__"

    def create(self, validated_data):
        return chatnombres.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance