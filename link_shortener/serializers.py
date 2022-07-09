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
        link = Link.objects.update_or_create(**validated_data)[0]
        link.users.add(self.context['request'].user)
        return link
