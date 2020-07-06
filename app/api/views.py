from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import User
from app.api.serializers import userSerializer


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = userSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = userSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' created successfully".format(user_saved.full_name)})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = userSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({
            "success": "User '{}' updated successfully".format(user_saved.full_name)
        })

    def delete(self, request, pk):
    	user = get_object_or_404(User.objects.all(), pk=pk)
    	user.delete()
    	return Response({
        	"message": "User with id `{}` has been deleted.".format(pk)
    	}, status=204)