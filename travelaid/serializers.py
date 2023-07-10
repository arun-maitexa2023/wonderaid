from rest_framework import serializers
from .models import log,user,Hotel,Restaurent,Resort,Travels,Guide

class loginUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = log
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'
    def create(self,validated_data):
        return user.objects.create(**validated_data)

class HotelRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
    def create(self,validated_data):
        return Hotel.objects.create(**validated_data)

class RestaurentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurent
        fields = '__all__'
    def create(self,validated_data):
        return Restaurent.objects.create(**validated_data)

class ResortRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resort
        fields = '__all__'
    def create(self,validated_data):
        return Resort.objects.create(**validated_data)

class TravelsRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travels
        fields = '__all__'
    def create(self,validated_data):
        return Travels.objects.create(**validated_data)

class GuideRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guide
        fields = '__all__'
    def create(self,validated_data):
        return Guide.objects.create(**validated_data)
