
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.db.models import Q, Count


from .serializers import SendMessageSerializer
from message.models import Message, UserMessage


class MessageView(generics.ListCreateAPIView):
    queryset = UserMessage.objects.all()
    serializer_class = SendMessageSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        return self.queryset.filter(Q(user=self.request.user) |Q(message__sent_by=self.request.user)).order_by('-created_at')

    def list(self, *args, **kwargs):
        data=[]
        for i in self.queryset.values('user__mobile').distinct():
            d = SendMessageSerializer(self.queryset.filter(user__mobile=i['user__mobile'], message__sent_by=self.request.user).order_by('-created_at'), many=True)
            data.append({i['user__mobile']:d.data})
        return Response(data=data)