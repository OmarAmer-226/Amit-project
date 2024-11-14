from django.urls import path
from . views import ProductsList,CreateProducts,UpdateProducts,DeleteProducts
from . views import BreakFastList,CreateBreakFast,UpdateBreakFast,DeleteBreakFast
from . views import MainDishesList,CreateMainDishes,UpdateMainDishes,DeleteMainDishes
from . views import DrinksList,CreateDrinks,UpdateDrinks,DeleteDrinks
from . views import DessertList,CreateDessert,UpdateDessert,DeleteDessert
from . views import TableBookingList,TableBookingCreate
# from . views import MyTokenObtainPairView
from .views import RegisterView, LoginView


urlpatterns =[
    # PRODUCTS URL
    path('products/', ProductsList.as_view(), name = 'products'),
    path('createProducts/',CreateProducts.as_view(), name = 'create'),
    path('updateProducts/<int:pk>/',UpdateProducts.as_view(), name = 'update'),
    path('deleteProducts/<int:pk>/',DeleteProducts.as_view(), name = 'delete'),
    # BREAKFAST URL
    path('BreakFast/', BreakFastList.as_view(), name = 'BreakFast'),
    path('createBreakfast/',CreateBreakFast.as_view(), name = 'create'),
    path('updateBreakfast/<int:pk>/',UpdateBreakFast.as_view(), name = 'update'),
    path('deleteBreakfast/<int:pk>/',DeleteBreakFast.as_view(), name = 'delete'),
    # MainDishes URL
    path('MainDishes/', MainDishesList.as_view(), name = 'MainDishes'),
    path('createMainDishes/',CreateMainDishes.as_view(), name = 'create'),
    path('updateMainDishes/<int:pk>/',UpdateMainDishes.as_view(), name = 'update'),
    path('deleteMainDishes/<int:pk>/',DeleteMainDishes.as_view(), name ='delete'),
   #DRINKS URL
    path('Drinks/', DrinksList.as_view(), name = 'Drinks'),
    path('createDrinks/', CreateDrinks.as_view(), name = 'create'),
    path('updateDrinks/<int:pk>/', UpdateDrinks.as_view(), name = 'update'),
    path('deleteDrinks/<int:pk>/', DeleteDrinks.as_view(), name = 'delete'),

    #Dessert URL
    path('Dessert/', DessertList.as_view(), name = 'Dessert'),  
    path('createDessert/', CreateDessert.as_view(), name = 'create'),  
    path('updateDessert/<int:pk>/', UpdateDessert.as_view(), name ='update'),
    path('deleteDessert/<int:pk>/', DeleteDessert.as_view(), name ='delete'),

    #BookTable URL
    path('bookTable/', TableBookingList.as_view(), name='book-table'),
    path('bookTableCreate', TableBookingCreate.as_view(), name='book-table-create'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
  
]


