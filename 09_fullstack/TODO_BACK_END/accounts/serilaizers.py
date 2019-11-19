from rest_framework import serializers
from django.contrib.auth import get_user_model

from todos.serilaizers import TodoSerializer

User = get_user_model()

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password',)


class UserSerializer(serializers.ModelSerializer):
    # 사용자 1명에 대한 serializer 이지만, 해당 user 의 Todos 를 모두 포함하여야 한다. 
    todo_set = TodoSerializer(many=True)  # 1:N 관계일때, 1에게 속한 모든 N을 가져온다. 
    class Meta:
        model = User
        fields = ('id', 'username', 'todo_set',)