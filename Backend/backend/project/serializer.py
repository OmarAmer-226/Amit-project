
from rest_framework import serializers
from .models import Breakfast,Products,MainDishes,Drinks,Dessert,TableBooking
from django.contrib.auth.models import User
# from rest_framework_simplejwt.tokens import RefreshToken



class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'  

class BreakFastSerializer(serializers.ModelSerializer):
    class Meta:
        model= Breakfast
        fields = '__all__'

class MainDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model= MainDishes
        fields = '__all__'

class DrinksSerializer(serializers.ModelSerializer):
    class Meta:
        model= Drinks
        fields = '__all__'

class DessertSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dessert
        fields = '__all__'



class TableBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableBooking
        fields = ['id','username', 'phone', 'date', 'time', 'total']




# class UserSerializer(serializers.ModelSerializer) :
#     name = serializers.SerializerMethodField(read_only = True) 
#     _id = serializers.SerializerMethodField(read_only = True) 
#     isAdmin = serializers.SerializerMethodField(read_only = True)
    
#     class Meta : 
#         model = User 
#         fields = ['_id' , 'username' , 'email' , "name" , 'isAdmin']
#     def get_name(self , obj ) :
#         name = obj.first_name 
#         if name == "" : 
#             name = obj.email
#         return name
#     def get__id(self , obj) : 
#         return obj.id
#     def get_isAdmin(self, obj) : 
#         return obj.is_staff

# class UserSerializerWithToken(UserSerializer) : 
#     token = serializers.SerializerMethodField(read_only = True)
#     class Meta : 
#         model = User 
#         fields = ['_id' , 'username' , 'email' , "name" , 'isAdmin' , 'token']
#     def get_token(self , obj) : 
#         token = RefreshToken.for_user(obj)
#         return str(token.access_token)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)