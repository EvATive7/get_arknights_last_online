import skland_api
import hypergryph_api
import datetime
import os
try:
    api = skland_api.SklandAPI(hypergryph_api.HypergryphAPI(input('phone: '), input('password: ')))
    list = api.get_binding_list_arknights()
    if len(list) != 1:
        choice_text = '\n'.join(["[{}][{}] {}".format(str(i+1), account['channelName'], account['nickName']) for i, account in enumerate(list)])
        uid = list[int(input(f'Multiple Arknights accounts\n{choice_text}\nPlease enter your option:'))-1]['uid']
    else:
        uid = list[0]['uid']
    print('Last online:', datetime.datetime.fromtimestamp(api.get_player_info(uid)['status']['lastOnlineTs']))
    os.system('pause')
except Exception as e:
    print(str(e))
