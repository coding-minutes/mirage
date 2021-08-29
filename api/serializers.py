from api.models import Links
from rest_framework import serializers


class LinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = "__all__"
