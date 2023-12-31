from review.models import Review
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    # _id = serializers.StringRelatedField(read_only=True)
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ('review_of', "_id")
