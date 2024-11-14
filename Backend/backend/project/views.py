from django.shortcuts import render
from .serializer import BreakFastSerializer,ProductsSerializer,MainDishesSerializer,DrinksSerializer,DessertSerializer,TableBookingSerializer,UserSerializer,LoginSerializer
from .models import Breakfast,Products,MainDishes,Drinks,Dessert,TableBooking
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.status import HTTP_201_CREATED , HTTP_400_BAD_REQUEST
from rest_framework.decorators import api_view , permission_classes
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# from rest_framework.views import APIView


# PRODUCTS VIEW
class ProductsList(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class CreateProducts(CreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

class UpdateProducts(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()

class DeleteProducts(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

def get(self, pk):
    products = Products.objects.get(pk=pk)
    serializer = ProductsSerializer(Products)
    return Response(serializer.data)

def destroy(self):
    instance = self.get_object()
    instance.delete()
    return Response({"massage:deleted"})


# BREAKFAST VIEW
class BreakFastList(ListAPIView):
    queryset = Breakfast.objects.all()
    serializer_class = BreakFastSerializer

class CreateBreakFast(CreateAPIView):
    queryset = Breakfast.objects.all()
    serializer_class = BreakFastSerializer

class UpdateBreakFast(UpdateAPIView):
    queryset = Breakfast.objects.all()
    serializer_class = BreakFastSerializer

def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()

class DeleteBreakFast(DestroyAPIView):
    queryset = Breakfast.objects.all()
    serializer_class = BreakFastSerializer

def get(self, pk):
    breakfast = Breakfast.objects.get(pk=pk)
    serializer = BreakFastSerializer(Breakfast)
    return Response(serializer.data)

def destroy(self):
    instance = self.get_object()
    instance.delete()
    return Response({"massage:deleted"})


class MainDishesList(ListAPIView):
    queryset = MainDishes.objects.all()
    serializer_class = MainDishesSerializer

class CreateMainDishes(CreateAPIView):
    queryset = MainDishes.objects.all()
    serializer_class = MainDishesSerializer

class UpdateMainDishes(UpdateAPIView):
    queryset = MainDishes.objects.all()
    serializer_class = MainDishesSerializer

def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()

class DeleteMainDishes(DestroyAPIView):
    queryset = MainDishes.objects.all()
    serializer_class = MainDishesSerializer

def get(self, pk):
    maidish = MainDishes.objects.get(pk=pk)
    serializer = MainDishesSerializer(MainDishes)
    return Response(serializer.data)

def destroy(self):
    instance = self.get_object()
    instance.delete()
    return Response({"massage:deleted"})


class DrinksList(ListAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

class CreateDrinks(CreateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

class UpdateDrinks(UpdateAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()

class DeleteDrinks(DestroyAPIView):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer

def get(self, pk):
    drinks = Drinks .objects.get(pk=pk)
    serializer = DrinksSerializer(Drinks)
    return Response(serializer.data)

def destroy(self):
    instance = self.get_object()
    instance.delete()
    return Response({"massage:deleted"})



class DessertList(ListAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

class CreateDessert(CreateAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

class UpdateDessert(UpdateAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

def update(self, request, *args, **kwargs):
    partial = kwargs.pop('partial', False)
    instance = self.get_object()
    serializer = self.get_serializer(instance, data=request.data, partial=partial)
    serializer.is_valid(raise_exception=True)
    self.perform_update(serializer)

    if getattr(instance, '_prefetched_objects_cache', None):
        instance._prefetched_objects_cache = {}
    return Response(serializer.data)

def perform_update(self, serializer):
    serializer.save()

class DeleteDessert(DestroyAPIView):
    queryset = Dessert.objects.all()
    serializer_class = DessertSerializer

def get(self, pk):
    dessert = Dessert .objects.get(pk=pk)
    serializer = DessertSerializer(Dessert)
    return Response(serializer.data)

def destroy(self):
    instance = self.get_object()
    instance.delete()
    return Response({"massage:deleted"})


class TableBookingList(ListAPIView):
    queryset = TableBooking.objects.all()
    serializer_class = TableBookingSerializer


class TableBookingCreate(CreateAPIView):
    def get(self, request):
        reservations = TableBooking.objects.all()
        serializer = TableBookingSerializer(reservations, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = TableBookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "msg": "Booking successful!"}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "msg": "Booking failed!", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            return Response({"message": "Login successful!"})
        else:
            return Response({"error": "Invalid credentials!"}, status=400)
        




        