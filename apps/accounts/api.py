from django.contrib.auth import get_user_model
from .models import Token

from rest_framework import status
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    UserDetailSerializer,
    LoginSerializer,
    UserCreateSerializer)

User = get_user_model()


class UserLoginAPIView(APIView):
    """
        使用账号或者密码进行登录
    """
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request):
        ser = self.serializer_class(data=request.data)
        if ser.is_valid():
            user = ser.user
            token = Token.objects.get_or_create(user=user)[0]
            data = {
                'code': 0,
                'msg': '恭喜您，登录成功',
                'token': token.key,
            }
        else:
            data = {
                'code': 1,
                'msg': '账号不存在或者密码错误'
            }
        return Response(data=data, status=status.HTTP_200_OK)


class UserCreateAPIView(APIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]
