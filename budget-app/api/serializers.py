from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import Budget, Item

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ['id','name','duration','archieved','budget_amount']

class AuthSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get(request),
                            email=email, password=password)
        attrs['user'] = user
        return attrs

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email','password')
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name','amount','budget']
