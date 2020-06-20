import json;
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name='room';
        self.room_group_name='chat_%s' %self.room_name;


        await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

        await self.accept();


    async def disconnect(self , close_code):
        await self.chennel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        bug = text_json_data['bug']
        creator = text_json_data['creator']
        body = text_json_data['body']
        comment = Comment.objects.create(bug=bug , creator = creator , body=body)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'bug' : bug,
                'creator':creator,
                'body':body
            }
        )



    async def chat_message(self , event):
        bug = event['bug']
        creator = event['creator']
        body = event['body']

        await self.send(text_data=json.dumps({'bug':bug , 'creator':creator , 'body':body}))

