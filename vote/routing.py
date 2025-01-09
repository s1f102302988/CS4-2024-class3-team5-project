from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/vote/kinokotakenoko/$", consumers.VoteConsumer.as_asgi()),
]
