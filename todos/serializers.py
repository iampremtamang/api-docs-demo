from rest_framework import serializers
from todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'is_completed', 'date_created', 'last_modified')
        read_only_fields = ('date_created', 'last_modified')
