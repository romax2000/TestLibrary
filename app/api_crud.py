from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view

import datetime
from app.decorators import define_usage
from app.models import User
from app.serializers import userSerializer


#URL /all/
@define_usage(returns={'users': 'Dict'})
@api_view(['GET'])
def api_all_users(request):
    users = userSerializer(User.objects.all(), many=True)
    return Response({'users': users.data})


#URL /new/
@define_usage(params={'full_name': 'String', 'middle_name': 'String', 'birth_day': 'Date', 'phone': 'String', 'email': 'String' },
              returns={'done': 'Bool'})
@api_view(['PUT'])
def api_new_user(request):
    user = User(full_name=request.data['full_name'], middle_name=request.data['middle_name'], birth_day=request.data['birth_day'], phone=request.data['phone'], email=request.data['email'])
    user.save()
    return Response({'done': True})


#URL /update/
@define_usage(params={'id': 'Int', 'full_name': 'String', 'middle_name': 'String', 'birth_day': 'Date', 'phone': 'String', 'email': 'String' },
              returns={'done': 'Bool'})
@api_view(['POST'])
def api_update_user(request):
    user = User.objects.get(id=request.data['id'])
    user.full_name = request.data['full_name']
    user.middle_name = request.data['middle_name']
    user.birth_day = request.data['birth_day']
    user.phone = request.data['phone']
    user.email = request.data['email']
    user.save()
    return Response({'done': True})


#URL /delete/
@define_usage(params={'id': 'Int'},
              returns={'done': 'Bool'})
@api_view(['DELETE'])
def api_delete_user(request):
    user = User.objects.get(id=request.data['id'])
    user.delete()
    return Response({'done': True})
