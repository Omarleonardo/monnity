from rest_framework import serializers
from authentication.models.userid import User

class UpdatePassSerializer(serializers.ModelSerializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)