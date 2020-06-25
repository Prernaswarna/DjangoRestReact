import json;
from channels.generic.websocket import AsyncWebsocketConsumer
from fixer.models import Comment , User , Bug
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async , async_to_sync

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
        await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    @database_sync_to_async
    def bug_element(self , pk):
        return Bug.objects.get(pk=pk)
    @database_sync_to_async
    def user_element(self ,pk):
        return User.objects.get(pk=pk)
    @database_sync_to_async
    def create_comment(self , bugelement , userelement , body):
        comment = Comment.objects.create(bug=bugelement , creator=userelement , body=body)

    async def receive(self,text_data):
        text_data_json = json.loads(text_data)
        bug = text_data_json['bug']
        creator = text_data_json['creator']
        body = text_data_json['body']
        print(bug)
        print(creator)
        print(body)
        bugelement = await self.bug_element(bug)
        userelement =await self.user_element(creator)
        print(bugelement)
        print(userelement)
        await self.create_comment(bugelement , userelement , body)
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

