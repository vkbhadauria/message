from rest_framework import serializers
from user.models import User, Group, GroupUser
from rest_framework.validators import UniqueTogetherValidator


class SignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  ['mobile', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =  ['mobile', 'password']

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields =  ['name', 'id']

    def get_current_user(self):
        request = self.context.get('request', None)
        return request.user.id

    def create(self, validated_data):
        validated_data['created_by_id'] = self.get_current_user()
        instance = super(GroupSerializer, self).create(validated_data)
        group_owner= GroupAddUserSerializer(data={'group_id': instance.id, 'user_id': validated_data['created_by_id']}, context=self.context)
        if group_owner.is_valid():
            group_owner.save()
        return instance

class GroupAddUserSerializer(serializers.ModelSerializer):
    group_id = serializers.CharField(write_only=True)
    user_id = serializers.CharField(write_only=True)

    class Meta:
        model = GroupUser
        fields = ['group_id', 'user_id']
        validators = [
                        UniqueTogetherValidator(
                            queryset=GroupUser.objects.all(),
                            fields = ['group_id', 'user_id']
                        )
                    ]
    def get_current_user(self):
        request = self.context.get('request', None)
        return request.user.id

    def validate_group_id(self, value):
        try:
            Group.objects.get(id=value, created_by_id=self.get_current_user())
        except:
            raise serializers.ValidationError("Not Authorized for this group")
        return value


class GroupJoinSerializer(serializers.ModelSerializer):
    group_id = serializers.CharField(write_only=True)
    
    class Meta:
        model = GroupUser
        fields = ['group_id']

    def validate_group_id(self, value):
        if GroupUser.objects.filter(group_id=value, user_id=self.get_current_user()):
            raise serializers.ValidationError("All ready Joined")
        return value

    def get_current_user(self):
        request = self.context.get('request', None)
        return request.user.id

    def create(self, validated_data):
        validated_data['user_id'] = self.get_current_user()
        return super(GroupJoinSerializer, self).create(validated_data)
        