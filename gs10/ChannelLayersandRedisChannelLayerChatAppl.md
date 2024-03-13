****Channel Layers
Channel layers allow you to talk between different instances of an application.
It is for high-level application-to-application communication.
A Channel Layer is the transport mechanism that allows multiple consumer instance to communicate with each other and other part of Django.
They're a useful part of making a distributed real-time application if you dont't want to have to shuttle all of your messages or events through a database.
    + Redis Channel Layer
    + In-Memory Channel Layer

+ Channels - Channelss are a first-in, first out queue with at-most-once delivery semantics,Each channel has a name.Messages are sent to channel by anyone who knows the channel name and the given to consumer listening on that channel.
+ Groups - Sending to individual channels isn't particularly useful - in most cases you'll want to send to multipal channels/consumers at once as a broadcast and there we use groups.
Multiple channels can be grouped into a group.Each group has a name. A channel can be added or removed from a group by anyone who knows the group name.Using the group name you can also send a message to all channels in the group.
Groups are a broadcast system that:
    - Allows you to add and remove channel names from named groups, and send to those named groups.
    - Provides group expiry for clean-up of connections whose disconnect handler didn't get to run(e.g.power failure)
+ Messages - Messages must be a dict.Because these messages are sometimes sent over a network,they need to be serializable.
***Redis Channel Layer
Redis works as the communication store for the channel layer.
In order to use Redis as a channel layer you have to install channels_redis package.
channels_redis is the only official Django-maintained channel layer supported for production use.
The layer uses Redis as its backing store,and supports both a single-server and sharded configurations,as well as group support.
***Config Redis Channel Layer
-Download and install Memurai-Redis for Windows alternative
-Install channels_redis - pip install channels_redis
- Open settings.py file then write
CHANNEL_LAYERS = {
    "default":{
        "BACKEND":"channels_redis.core.RedisChannelLayer",
        "CONFIG":{
            "hosts":[("127.0.0.1",6379)],
        },
    },
}

***Channel Layer
+ get_channel_layer() - This function is used to get default channel layer from a project.from channels.layers import get_channel_layer

+ Channel_layer - This attribute is used to get default channel layer from a project.This contains a pointer to the channel layer instance, only if you are using consumers.

+ channel_name -This attribute contains the channel name thet will reach the consumer.

+ send() - It that takes two arguments: the channel to send on ,as a unicode string, and the message to send ,as a serializable dict.
Syntax : -send('channel_name',message) 

+ group_send() - It takes two positional arguments; the group to send to, as a unicode string,and the message to send, as a serializable dict. It may raise MessageTooLarge but cannot raise ChannelFull.
Syntax :-group_send('group_name',message)
group_add() - This is used to add a channel to a new or existing group.If the channel is already in the group,the function should return normally.
Syntax:-group_add('group_name','channel_name')
Example :- group_add('friends',self.channel_name)

group_discard()- This is used to remove channel from the group if it is in it,and dose nothing otherwise.
Syntax:- group_discard('group_name','channel_name')
Example:-group_discard('friends',self.channel_name)
+ MessageTooLarge,the exception raised when a send operation fails because the encoded message is over the layer's size limit.
+ ChannelFull,the exception raised when a send operation fails because the destination channel is over capacity.


  












