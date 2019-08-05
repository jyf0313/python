# 导入电脑版微信模块
import itchat
# 自动登录，hotReload='True'表示长时间登录，5分钟左右
itchat.auto_login(hotReload='True')
# 获取所有好友信息，返回的是以dict为元素的list
friends_info = itchat.get_friends(update='True')
# 定义变量，男，女，中性人员数量
man = 0
woman = 0
neutral = 0
# 遍历每一个好友的信息，搜索关键字sex, 提取性别数量，判断性别，对应性别加1
for i in friends_info:
    print(i)
    # 如果是男，man+1
    if i['Sex'] == 1:
        man += 1
    # 如果是女， woman+1
    if i['Sex'] == 2:
        woman += 1
    # 如果是中， neutral+1
    if i['Sex'] == 0:
        neutral += 1
print(man, woman, neutral)
# 计算他们的比例, 百分比 *100
man_per = man/(man + woman + neutral) * 100
woman_per = woman/(man + woman + neutral) * 100
neutral_per = neutral/(man + woman + neutral) * 100
# 打印，保留小数点后一位
print('好友男性比例: %.1f'%man_per + '%')
print('好友女性比例: %.1f'%woman_per + '%')
print('好友中性比例: %.1f'%neutral_per + '%')
# 把这个内容发给指定的好友
# 搜索备注为'邬建珍'的人，返回的是一个list, 且打印有多少的元素
friends_search_wujianzhen = itchat.search_friends(remarkName= '邬建珍')
print(friends_search_wujianzhen)
print(len(friends_search_wujianzhen))
# 由于只搜索到一位，只要索引[0]就可以获取这个元素
friends_wujianzhen_only = friends_search_wujianzhen[0]
# 发送消息的参数必须为UserName，所以接着索引元素的关键字UserName获取内容
friends_wujianzhen_only_username = friends_search_wujianzhen[0]['UserName']
# 发送内容
itchat.send_msg('好友男性比例: %.1f'%man_per + '%', toUserName=friends_wujianzhen_only_username)
itchat.send_msg('好友女性比例: %.1f'%woman_per + '%', toUserName=friends_wujianzhen_only_username)
itchat.send_msg('好友中性比例: %.1f'%neutral_per + '%', toUserName=friends_wujianzhen_only_username)





