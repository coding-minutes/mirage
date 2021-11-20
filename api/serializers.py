from api.models import Links
from rest_framework import serializers


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"

    def update(self, instance, validated_data):
        if "author" in validated_data:
            raise serializers.ValidationError({
                "message" : "You cannot update the `author` field"
            })
        return super().update(instance, validated_data)
