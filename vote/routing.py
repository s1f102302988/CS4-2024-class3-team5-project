from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"cs4-2024-class3-team5-project/vote/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]