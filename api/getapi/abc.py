from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class SignupPage(APIView):
        def get(self, request):
            model = Signup.objects.all()
            serializer = SignUpSerializer(model, many=True)
            return Response(serializer.data)

        def post(self, request):

            serializer = SignUpSerializer(data=request.data)
            if serializer.is_valid():
               serializer.save()
               return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignupPageUserDetails(APIView):
    def get_user(self, passengers_id):
        try:
            model = Signup.objects.get(id= passengers_id)
            return model
        except Signup.DoesNotExit:
            return 
    



    def get(self, request, passangers_id):

        serializer = SignUpSerializer(self.get_user(passangers_id))
        return Response(serializer.data)


    def put(self, request, passangers_id):
        serializer = SignUpSerializer(self.get_user(passangers_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, passengers_id):
        model = self.get_user(passengers_id)
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


