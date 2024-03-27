from rest_framework.serializers import ModelSerializer

from .models import Category, Operation


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OperationSerializer(ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Operation
        fields = '__all__'
