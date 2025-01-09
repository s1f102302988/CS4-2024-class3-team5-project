from channels.generic.websocket import AsyncWebsocketConsumer
import json

class VoteConsumer(AsyncWebsocketConsumer):
    votes = {'kinoko': 0, 'takenoko': 0}

    async def connect(self):
        self.group_name = 'vote_group'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        if message in self.votes:
            self.votes[message] += 1

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send_vote_data',
                'kinoko': self.votes['kinoko'],
                'takenoko': self.votes['takenoko'],
            }
        )
    async def send_vote_data(self, event):
        await self.send(text_data=json.dumps({
            'kinoko': event['kinoko'],
            'takenoko': event['takenoko'],
        }))

class KinokoTakenokoConsumer(AsyncWebsocketConsumer):
    votes = {"kinoko": 0, "takenoko": 0}

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        vote_item = data.get('message')

        if vote_item in self.votes:
            self.votes[vote_item] += 1

        # クライアントに投票結果を送信
        await self.send(text_data=json.dumps(self.votes))


# 愛 vs お金
class LoveOrMoneyConsumer(AsyncWebsocketConsumer):
    votes = {"love": 0, "money": 0}

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        vote_item = data.get('message')

        if vote_item in self.votes:
            self.votes[vote_item] += 1

        # クライアントに投票結果を送信
        await self.send(text_data=json.dumps(self.votes))


# トロッコ問題
class TorokkoConsumer(AsyncWebsocketConsumer):
    votes = {"option1": 0, "option2": 0}

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        vote_item = data.get('message')

        if vote_item in self.votes:
            self.votes[vote_item] += 1

        # クライアントに投票結果を送信
        await self.send(text_data=json.dumps(self.votes))

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))