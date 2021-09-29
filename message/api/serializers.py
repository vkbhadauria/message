from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from message.models import Message, UserMessage
from user.models import User, Group, GroupUser


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields =  ['text', 'media', 'message_type', 'uuid']

    def get_current_user(self):
        request = self.context.get('request', None)
        return request.user

    def create(self, validated_data):
        validated_data['sent_by'] = self.get_current_user()
        return super(MessageSerializer, self).create(validated_data)


class SendMessageSerializer(serializers.ModelSerializer):
    message = MessageSerializer()
    reciever_mobile = serializers.CharField(allow_blank=True, write_only=True)
    sender = serializers.SerializerMethodField()
    reciever = serializers.SerializerMethodField()
    class Meta:
        model = UserMessage
        fields = ['message', 'sender', 'reciever_mobile','reciever']

    def get_reciever(self, obj):
        return obj.user.mobile

    def get_current_user(self):
        request = self.context.get('request', None)
        return request.user.id

    def get_sender(self, obj):
        return obj.message.sent_by.mobile


    def create(self, validated_data):
        current_user  = self.get_current_user()
        instance =None
        msg = MessageSerializer(data=validated_data.pop('message'), context=self.context)
        if msg.is_valid():
            validated_data['message']=msg.save()
        if validated_data.get('group_id'):
            user_id = GroupUser.objects.filter(group_id=validated_data.get('group_id')).values_list('user_id', flat=True)
        else:
            user, is_created = User.objects.get_or_create(mobile=validated_data.pop('reciever_mobile'))
            user_id = [user.id]
        for user in user_id:
            validated_data['user_id'] = user
            obj = super(SendMessageSerializer, self).create(validated_data)
        return obj
