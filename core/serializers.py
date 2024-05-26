# Importing necessary modules
from rest_framework import serializers
from .models import Account, Destination
import json

# Serializer for the Account model
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'  # Serializes all fields of the Account model

# Custom JSON serializer field to handle JSON data in serializers
class JSONSerializerField(serializers.Field):
    def to_representation(self, value):
        # Convert string to JSON object before representation
        if isinstance(value, str):
            return json.loads(value)
        return value

    def to_internal_value(self, data):
        # Convert JSON data to Python object before storing internally
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Invalid JSON format")
        return data

# Serializer for the Destination model
class DestinationSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField to serialize the account ID
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    # Using custom JSONSerializerField to handle JSON data for headers
    headers = JSONSerializerField()

    class Meta:
        model = Destination
        fields = '__all__'  # Serializes all fields of the Destination model
