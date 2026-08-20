from django.shortcuts import get_object_or_404
from celery import shared_task
from .models import DrawLog, Room
from authentication.models import Profile

@shared_task
def Logging(x, y, user, room_id):
    profile_data=Profile.objects.get(user=user)
    room_data=Room.objects.get(id=room_id)
    DrawLog.objects.create(user=profile_data, room=room_data, x_position=x, y_position=y)
    return "Data successfully added in the logs"