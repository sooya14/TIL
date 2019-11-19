from django.shortcuts import get_object_or_404

from rest_framework.response import Response  # JSON 응답 생성기
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 회원가입은, 인증을 볼 필요가 없음.

from .serilaizers import UserCreationSerializer, UserSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserCreationSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()  # 최초 저장 후, 
        user.set_password(user.password)  # password 암호화하기 위해서 갈아끼운다. 
        user.save()
        return Response(status=200, data={'message': '회원가입 성공'})  # message => postman 에서 보기 위해서 설정(사용자는 볼 수 없다. )


@api_view(['GET'])
def my_todos(request):
    user = request.user  # JWT 를 통해서, 요청보낸 사용자를 잡아낸다. 
    serializer = UserSerializer(user)
    return Response(serializer.data)

        