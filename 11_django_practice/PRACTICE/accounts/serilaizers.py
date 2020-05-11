from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# 회원가입 
class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'username', 'password', 'age', 'gender', 'kakao_id')
        fields = '__all__'