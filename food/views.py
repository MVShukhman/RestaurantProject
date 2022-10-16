from .services import get_filtered_foods_in_categories
from rest_framework import generics
from rest_framework.response import Response


class FoodListView(generics.GenericAPIView):
    name = "Menu"

    def get(self, *args, **kwagrs):
        return Response({"Categories": get_filtered_foods_in_categories()})
