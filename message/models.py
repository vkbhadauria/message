from django.db import models
from user.models import User, Group
from common.models import TimeModel
import uuid


class Message(TimeModel):
	MESSAGE_TYPE = (
			('text', 'text'),
			('media', 'media'),
		)
	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	text = models.CharField(max_length=350, null=True, blank=True)
	media = models.FileField(upload_to='uploads/', null=True, blank=True)
	sent_by = models.ForeignKey(User, related_name='sent_by', on_delete=models.CASCADE)
	message_type = models.CharField(max_length=10, choices=MESSAGE_TYPE, default='text')

	def __str__(self):
		return f'{self.text if self.text else self.message_type}'

class UserMessage(TimeModel):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reciever_mobile', null=True, blank=True)
	message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message')
	group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name='user_message_group')
	is_readed = models.BooleanField(default=False)
	

	def __str__(self):
		return f'{self.id}:{self.user}:{self.message}'



