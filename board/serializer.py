from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from authentication.serializers import ProfileGetSerializer
from .models import RoomMember, Room

class RoomGetSerializer(ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class RoomSerializer(ModelSerializer):
    class Meta:
        model=Room
        fields=['name']

class RoomMemberGetSerializer(ModelSerializer):
    room=RoomGetSerializer(read_only=True)
    user=ProfileGetSerializer(read_only=True)
    class Meta:
        model=RoomMember
        fields='__all__'

class RoomMemberSerializer(ModelSerializer):
    room=PrimaryKeyRelatedField(queryset=Room.objects.all())
    class Meta:
        model=RoomMember
        fields=['room', 'user']
        read_only_fields=['user']