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
        link = Link.objects.update_or_create(**validated_data)[0]
        if user.is_authenticated:
            link.users.add(self.context['request'].user)
        return link
