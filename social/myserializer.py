from rest_framework import serializers
from social.models import MyProfile, MyPost, PostLike, FollowUser, AddConfession, Vithub, Contact, Chat, Developer, Poll, PollVoted

class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProfile
        fields = '__all__'

class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPost
        fields = '__all__'

class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = '__all__'

class FollowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUser
        fields = '__all__'

class AddConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddConfession
        fields = '__all__'

class VithubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vithub
        fields = '__all__'
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = '__all__'

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = '__all__'

class PollVotedSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollVoted
        fields = '__all__'


# from rest_framework import serializers
# from social.models import MyProfile, MyPost, PostComment, PostLike, FollowUser
# from django.contrib.auth.models import User

# class MyProfile(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MyProfile
#         fields = "__all__"
    
# class MyPost(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = MyPost
#         fields = "__all__"
    
# class PostComment(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PostComment
#         fields = "__all__"
    
# class PostLike(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PostLike
#         fields = "__all__"
    
# class FollowUser(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = FollowUser
#         fields = "__all__"

