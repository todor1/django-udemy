from email.mime import image
from rest_framework import serializers
from .models import MovieData


class MovieDataSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = MovieData
        # fields = "__all__"
        fields = ["id", "name", "duration", "rating", "year", "genre", "image"]
