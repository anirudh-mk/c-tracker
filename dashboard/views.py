from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from utils.permission import TokenGenerate
from utils.response import CustomResponse


# Create your views here.


class CreateUserAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        serializer = UserCreateSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()

            return CustomResponse(
                general_message='User created successfully'
            ).get_success_response()

        return CustomResponse(
            response=serializer.errors
        ).get_failure_response()


class UserLoginAPI(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if email is None or password is None:
            return CustomResponse(
                general_message='email and password is required'
            ).get_failure_response()

        user = authenticate(request, email=email, password=password)

        if user:
            auth = TokenGenerate().generate(user)
            return CustomResponse(
                general_message="successfully login",
                response=[auth, {"is_admin": user.is_admin}],
            ).get_success_response()
        else:
            return CustomResponse(
                general_message="login failed"
            ).get_failure_response()
