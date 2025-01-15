from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
re_path(r"ws/vote/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
# きのこ vs たけのこ
re_path(r'^ws/vote/kinokotakenoko/$', consumers.KinokoTakenokoConsumer.as_asgi()),
# 愛 vs 金
re_path(r'^ws/vote/loveormoney/$', consumers.LoveOrMoneyConsumer.as_asgi()),
# トロッコ
re_path(r'^ws/vote/torokko/$', consumers.TorokkoConsumer.as_asgi()),
]
