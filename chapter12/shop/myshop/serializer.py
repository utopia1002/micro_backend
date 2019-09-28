from rest_framework import serializers
from myshop.models import Category, Real_estate, MyUser

class CateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class RS_Serializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url= True)
    class Meta:
        model = Real_estate
        fields = ('id','name','detail','image','price','category','like')

class RS_detail_Serializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url= True)
    class Meta:
        model = Real_estate
        fields = '__all__'

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email','name')
