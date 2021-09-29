from django.urls import path

from .user_views import SignupView, LoginView
from .group_views import GroupView, GroupJoinView, GroupAddUserView

urlpatterns = [
	path('signup', SignupView.as_view()),
	path('login', LoginView.as_view()),
	# path('group', GroupView.as_view()),
	# path('groupadduser',GroupAddUserView.as_view()),
	# path('groupjoin', GroupJoinView.as_view())
]