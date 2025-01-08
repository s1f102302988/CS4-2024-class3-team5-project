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

    def handle_vote_message(self, message):
        vote_type = message.get('type')
        vote_item = message.get('message')

        if vote_type == 'kinokotakenoko':
            # きのこ vs たけのこ 投票処理
            self.update_kinoko_takenoko_votes(vote_item)
        elif vote_type == 'loveormoney':
            # 愛 vs 金 投票処理
            self.update_love_money_votes(vote_item)
        elif vote_type == 'trolleyproblem':
            # トロッコ問題 投票処理
            self.update_trolley_problem_votes(vote_item)

    def update_kinoko_takenoko_votes(self, vote_item):
        # 投票の更新処理を記述
        pass

    def update_love_money_votes(self, vote_item):
        # 投票の更新処理を記述
        pass

    def update_trolley_problem_votes(self, vote_item):
        # 投票の更新処理を記述
        pass



