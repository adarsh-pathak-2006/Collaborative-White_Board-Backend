from django.shortcuts import get_object_or_404
from .serializer import RoomGetSerializer, RoomSerializer, RoomMemberGetSerializer, RoomMemberSerializer
from .models import Room, RoomMember
from authentication.models import Profile
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ALLRoomAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return RoomSerializer
    queryset=Room.objects.all()

    def perform_create(self, serializer):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        room_data=serializer.save(created_by=profile_data)
        RoomMember.objects.create(room=room_data, user=profile_data, is_admin=True)

class DetailRoomAPI(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return RoomSerializer   

    def get_queryset(self):
        if self.request.method=='GET':
            return Room.objects.all()
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Room.objects.filter(created_by=profile_data)

class RoomMemberListAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        room_data=get_object_or_404(Room, id=pk)
        data=RoomMember.objects.filter(room=room_data)
        serial=RoomMemberGetSerializer(data, many=True)
        return Response(serial.data, status=200)

    def post(self, request, pk):
        room_data = get_object_or_404(Room, id=pk)
        if RoomMember.objects.filter(room=room_data).count() >= 2:
            return Response({"error": "Room is full. Maximum 2 members allowed."},status=400)
        
        serial=RoomMemberSerializer(data=request.data)
        if serial.is_valid():
            profile_data=get_object_or_404(Profile, user=request.user)
            serial.save(user=profile_data)
            return Response(serial.data, status=201)
        return Response(serial.errors, status=400)   
            
