from django.shortcuts import get_object_or_404

from rest_framework.response import Response  # JSON 응답 생성기
from rest_framework.decorators import api_view # require_methods

from .models import Todo
from .serilaizers import TodoSerializer


# @api_view(['GET'])
# def todo_list(request):
#     serializer = TodoSerializer



@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)  # request.POST => form-data 만 잡는다.
    if serializer.is_valid():
        serializer.save(user=request.user)  # header 에 있는 token 으로 알아서 user 판별해준다. 
        # serializer.data => {'id': 1, 'user_id': 1, 'title': '밥먹기', 'completed': false }
        return Response(serializer.data)

    return Response(status=400, data=serializer.errors)    


@api_view(['PATCH', 'DELETE'])
def update_delete_todo(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)

    if request.method == 'PATCH':
        serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=400, data=serializer.errors)

    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=204)  # 204: 콘텐츠가 없다. 

