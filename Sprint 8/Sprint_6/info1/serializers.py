from rest_framework import serializers
from info1.models import Infoinsta


class info1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Infoinsta
        fields = "__all__"

    def create(self, validated_data):
        return Infoinsta.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nick_name = validated_data.get('nick_name', instance.nick_name)
        instance.arroba = validated_data.get('arroba', instance.arroba)
        instance.biography = validated_data.get('biography', instance.biography)
        instance.followers = validated_data.get('followers', instance.followers)
        instance.followeds = validated_data.get('followeds', instance.followeds)
        instance.publications = validated_data.get('publications', instance.publications)
        instance.url = validated_data.get('url', instance.url)
        instance.save()
        return instance