from rest_framework import serializers
from .models import Account, Destination
import json

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class JSONSerializerField(serializers.Field):
    def to_representation(self, value):
        if isinstance(value, str):
            return json.loads(value)
        return value

    def to_internal_value(self, data):
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                raise serializers.ValidationError("Invalid JSON format")
        return data

class DestinationSerializer(serializers.ModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    headers = JSONSerializerField()

    class Meta:
        model = Destination
        fields = '__all__'
