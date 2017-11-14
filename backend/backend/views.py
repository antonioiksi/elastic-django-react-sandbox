from django.contrib.auth.models import User
from django.urls import resolve
from rest_framework import serializers, views, status, generics
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app_log.mixins import RequestLogViewMixin

from .serializers import UserSerializer, MessageSerializer


class TokenObtainPairWithLoggingView(RequestLogViewMixin, TokenObtainPairView):
    """
    Keep obtaining JWT token through Logging middleware.
    """


class TokenRefreshViewLoggingView(RequestLogViewMixin, TokenRefreshView):
    """
    Keep refreshing JWT token through Logging middleware.
    """



class CurrentUserView(RequestLogViewMixin, generics.ListAPIView):
    """
    Get current user info
    """
    serializer_class = UserSerializer
    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.pk)



class EchoView(views.APIView):
    """
    post:
    load message via post method
    """
    def post(self, request, *args, **kwargs):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED)

