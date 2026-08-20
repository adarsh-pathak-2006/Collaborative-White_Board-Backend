from django.urls import path
from .views import ALLRoomAPI, DetailRoomAPI, RoomMemberListAPI

urlpatterns = [
    path('rooms/', ALLRoomAPI.as_view(), name='all_room'),
    path('rooms/<int:pk>/', DetailRoomAPI.as_view(), name='detail_room'),
    path('room-members/<int:pk>/', RoomMemberListAPI.as_view(), name='room_member_list'),
]
