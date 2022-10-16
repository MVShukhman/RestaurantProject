from .models import FoodCategory
from .serializers import FoodListSerializer


def get_filtered_foods_in_categories():
    full_data = FoodListSerializer(FoodCategory.objects.all(), many=True).data
    ans_data = []
    for category in full_data:
        foods_to_publish = [
            food for food in category["foods"] if food.pop("is_publish")
        ]
        if len(foods_to_publish):
            category["foods"] = foods_to_publish
            ans_data.append(category)
    return ans_data
