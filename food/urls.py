from django.urls import path, include
from .views import *

app_name = "food"
urlpatterns = [
    path("food/", FoodListView.as_view()),
]
