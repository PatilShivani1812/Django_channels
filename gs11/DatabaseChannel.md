The Django ORM is a synchronous piece of code, and so if you  want to access it from asynchronous code you need to do special handling to make sure its connections are closed properly.
If you 're using SyncConsumer, or anything based on it -like JsonWebsocketConsumer-you don't need to do anything special,as all your code is already run in a synchronous mode and channels will do the cleanup for you as part of the SyncConsumer code.
If you are writing asynchronous code,however,you will need to call database methods in a safe,synchronous context,using database_sync_to_async.


***database_sync_to_async
Write your ORM queries in a separate function or method,and then call it with database_sync_to_async.
Example:-
from channels.db import database_sync_to_async
async def websocket_connect(self):
    self.username = await database_sync_to_async(self.get_name)()

def get_name(self):
    return User.objects.all()[0].name

Use it as decorator
@database_sync_to_async
def get_name(self):
    return User.objects.all()[0].name
    