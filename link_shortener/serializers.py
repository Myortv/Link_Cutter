from rest_framework import serializers

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    hashed_url = serializers.SlugField(read_only=True)
    class Meta:
        model = Link
        fields = (
            'original_link',
            'hashed_url',
        )


    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            link = Link.objects.create(**validated_data, user=user)
        else:
            link = Link.objects.create(**validated_data, user=None)
        return link
