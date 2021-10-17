from mirai import *
import top
import top.api
import re

if __name__ == '__main__':
    bot = Mirai(qq=822494832, adapter=WebSocketAdapter(
        verify_key="myvfKey",
        host='localhost',
        port=8081
    ))

    find_req = top.api.TbkDgMaterialOptionalRequest()
    find_req.set_app_info(top.appinfo('33082016', 'df6564cdf0c69b64581f915c4b770324'))
    find_req.adzone_id = '111713900272'
    find_req.sort = 'match_des'

    ring_req = top.api.TbkTpwdCreateRequest()
    ring_req.set_app_info(top.appinfo('33082016', 'df6564cdf0c69b64581f915c4b770324'))

    @bot.on(MessageEvent)
    async def repeat_message(event: MessageEvent):
        if event.sender.id in [2107665794, 1357495247, 2656227409]:
            return
        if (not (re.search('[0-9a-zA-Z]{11}', str(event.message_chain)) and len(str(event.message_chain)) > 11)) and (At(bot.qq) not in event.message_chain):
            return
        if At(bot.qq) in event.message_chain:
            find_req.q = str(event.message_chain[Plain])
        else:
            find_req.q = re.sub(u"([^\u4e00-\u9fa5])", "", str(event.message_chain[Plain]))
        try:
            cnt = 0
            for i in find_req.getResponse()['tbk_dg_material_optional_response']['result_list']['map_data']:
                # await bot.send(event, i['title'] + ' https:' + i['url'])
                try:
                    if 'coupon_share_url' in i:
                        ring_req.url = 'https:' + i['coupon_share_url']
                    else:
                        ring_req.url = 'https:' + i['url']
                    await bot.send(event, ring_req.getResponse()['tbk_tpwd_create_response']['data']['model'], quote=True)
                except Exception as e:
                    return bot.send(event, str(e))
                cnt += 1
                if cnt == 2:
                    break
            return
        except Exception as e:
            return bot.send(event, str(e))

    bot.run()