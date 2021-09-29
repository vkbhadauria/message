
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


from .serializers import GroupSerializer, GroupJoinSerializer, GroupAddUserSerializer
from user.models import Group, GroupUser


class GroupView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(created_by=self.request.user).order_by('-created_at')

class GroupJoinView(generics.CreateAPIView):
    queryset = GroupUser.objects.all()
    serializer_class  = GroupJoinSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

class GroupAddUserView(generics.CreateAPIView):
    queryset = GroupUser.objects.all()
    serializer_class  = GroupAddUserSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]