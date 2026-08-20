from django.db import models
from authentication.models import Profile

class Room(models.Model):
    created_by=models.ForeignKey(Profile, on_delete=models.CASCADE)
    name=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class RoomMember(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_admin=models.BooleanField(default=False)
    added_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints=[models.UniqueConstraint(fields=['room', 'user'], name='unique_user_per_room')]

    def __str__(self):
        return f"{self.user.name} in room {self.room.name}"

class DrawLog(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    x_position=models.IntegerField()
    y_position=models.IntegerField()
    added_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} of {self.room.name}"