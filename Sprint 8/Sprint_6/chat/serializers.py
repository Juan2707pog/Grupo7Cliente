from rest_framework import serializers
from chat.models import chatnombres
from info1.serializers import info1Serializer


class ChatSerializer(serializers.ModelSerializer):
    
    first_name = serializers.CharField(max_length=100, required=True)
    last_name = serializers.CharField(max_length=20, required=True)
    asd = info1Serializer(required = True)

    class Meta:
        model = chatnombres
        fields = "__all__"

    def create(self, validated_data):
        return chatnombres.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.asd = validated_data.get('asd', instance.asd)
        instance.save()
        return instance