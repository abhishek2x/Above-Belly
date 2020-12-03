from social.models import *
from rest_framework import viewsets, permissions
from .myserializer import *


class MyProfileViewSet(viewsets.ModelViewSet):
    queryset = MyProfile.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyProfileSerializer

class MyPostViewSet(viewsets.ModelViewSet):
    queryset = MyPost.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MyPostSerializer


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostLikeSerializer


class FollowUserViewSet(viewsets.ModelViewSet):
    queryset = FollowUser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FollowUserSerializer


class AddConfessionViewSet(viewsets.ModelViewSet):
    queryset = AddConfession.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AddConfessionSerializer


class VithubViewSet(viewsets.ModelViewSet):
    queryset = Vithub.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VithubSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ChatSerializer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = DeveloperSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PollSerializer


class PollVotedViewSet(viewsets.ModelViewSet):
    queryset = PollVoted.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PollVotedSerializer

