from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.permissions import (AllowAny, IsAuthenticated)
from rest_framework.response import Response
from rest_framework.views import APIView

User = get_user_model()
