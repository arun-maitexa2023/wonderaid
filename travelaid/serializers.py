from rest_framework import serializers
from .models import log,user,Hotel,Restaurent,Resort,Travels,Guide,Spots,Userprofile,Plannedtrip,Comments,Notification,PackegeHotel,PackegeResort,PackegeTravels,Chatcommunity,Reels,Resortbooking,Hotelbooking

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

class SpotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spots
        fields = '__all__'
    def create(self,validated_data):
        return Spots.objects.create(**validated_data)

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = '__all__'
    def create(self,validated_data):
        return Userprofile.objects.create(**validated_data)

class PlannedtripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plannedtrip
        fields = '__all__'
    def create(self,validated_data):
        return Plannedtrip.objects.create(**validated_data)

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'
    def create(self,validated_data):
        return Comments.objects.create(**validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
    def create(self,validated_data):
        return Notification.objects.create(**validated_data)

class PackegeHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackegeHotel
        fields = '__all__'
    def create(self,validated_data):
        return PackegeHotel.objects.create(**validated_data)


class PackegeResortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackegeResort
        fields = '__all__'
    def create(self,validated_data):
        return PackegeResort.objects.create(**validated_data)


class PackegeTravelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackegeTravels
        fields = '__all__'
    def create(self,validated_data):
        return PackegeTravels.objects.create(**validated_data)



class ChatcommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Chatcommunity
        fields = '__all__'
    def create(self,validated_data):
        return Chatcommunity.objects.create(**validated_data)

class ReelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reels
        fields = '__all__'
    def create(self,validated_data):
        return Reels.objects.create(**validated_data)


class ResortbookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resortbooking
        fields = '__all__'
    def create(self,validated_data):
        return Resortbooking.objects.create(**validated_data)


class HotelbookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotelbooking
        fields = '__all__'
    def create(self,validated_data):
        return Hotelbooking.objects.create(**validated_data)
