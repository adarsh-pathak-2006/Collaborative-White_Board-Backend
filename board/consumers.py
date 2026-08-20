import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RoomMember, Room
from authentication.models import Profile
from board.tasks import Logging

class DrawingBoardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user=self.scope['user']
        if self.user.is_authenticated:
            self.room_id=self.scope['url_route']['kwargs']['rid']
            room_data=await Room.objects.aget(id=self.room_id)
            profile_data=await Profile.objects.aget(user=self.user)
            if await RoomMember.objects.filter(room=room_data, user=profile_data).aexists():
                await self.accept()
                self.group_name=f"user_of_{self.room_id}"
                await self.channel_layer.group_add(self.group_name, self.channel_name)
                return
            await self.close()
            return "user is not a part of the group"
        await self.close()
        return "user is not authenticated"

    async def receive(self, text_data):
        board_data=json.loads(text_data)
        x_position=board_data.get("x_position")
        y_position=board_data.get("y_position")

        await self.channel_layer.group_send(self.group_name, {"type":"positions", "x_position":x_position, "y_position":y_position})

    async def positions(self, event):
        await self.send(text_data=json.dumps({"x_position":event["x_position"], "y_position":event["y_position"]}))
        Logging.delay(x=event['x_position'], y=event['y_position'], user_id=self.user.id, room_id=self.room_id)

    async def disconnect(self, code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

        
            