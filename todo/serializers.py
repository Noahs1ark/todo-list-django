from rest_framework import serializers
from .models import Task
from .models import Category

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'heading', 'description', 'completed', 'due', 'created', 'modified', 'category', 'user']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
