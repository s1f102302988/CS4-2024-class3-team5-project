from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VoteConsumer(AsyncWebsocketConsumer):
    votes = {'kinoko': 0, 'takenoko': 0}  # 投票数の管理

    async def connect(self):
        self.group_name = 'vote_group'
        # グループにクライアントを追加
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # グループからクライアントを削除
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        if message in self.votes:
            self.votes[message] += 1

        # 投票結果をすべてのクライアントに送信
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_vote_data',
                'kinoko': self.votes['kinoko'],
                'takenoko': self.votes['takenoko'],
            }
        )

    async def send_vote_data(self, event):
        # クライアントに投票結果を送信
        await self.send(text_data=json.dumps({
            'kinoko': event['kinoko'],
            'takenoko': event['takenoko'],
        }))

