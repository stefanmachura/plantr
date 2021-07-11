from photos.models import Photo

from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ["id", "published_at", "modified_at", "temp_file", "s3_url"]