from mirai import *

if __name__ == '__main__':
    bot = Mirai(qq=822494832, adapter=WebSocketAdapter(
        verify_key="myvfKey",
        host='localhost',
        port=8081
    ))

    @bot.on(MessageEvent)
    async def repeat_message(event: MessageEvent):
        return bot.send(event, MessageChain(['进行一个复读的工作']) + event.message_chain)

    bot.run()