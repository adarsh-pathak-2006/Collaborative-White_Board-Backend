from django.urls import path
from .consumers import DrawingBoardConsumer

websocket_urlpatterns=[
    path('ws/room/<int:rid>/', DrawingBoardConsumer.as_asgi(), name='drawing_board_consumer')
]

