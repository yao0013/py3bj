import requests
from bs4 import  BeautifulSoup

res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=55694644864407925&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
# 请求html，得到response
res_music.encoding = 'utf-8'

json_music = res_music.json()

list_music = json_music['data']['song']['list']
# 一层一层地取字典，获取歌单列表
for music in list_music:
# 对查找的结果执行循环
    print(music['name'])
    # 打印出我们想要的音乐名
    print('所属专辑：'+music['album']['name'])
    # 查找专辑名
    print('播放时长：'+str(music['interval'])+'秒')
    # 查找播放时长
    print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
    # 查找播放链接