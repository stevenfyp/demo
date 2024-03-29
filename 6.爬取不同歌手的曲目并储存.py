import requests
#调用requests模块
import time
import openpyxl
name = input('请输入歌手名字：')
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = (name)
sheet['A1'] ='歌曲名'     #加表头，给A1单元格赋值
sheet['B1'] ='所属专辑'   #加表头，给B1单元格赋值
sheet['C1'] ='播放时长'   #加表头，给C1单元格赋值
sheet['D1'] ='播放链接'   #加表头，给D1单元格赋值
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(2):
    time.sleep(2)
    headers = {
        'origin': 'https://y.qq.com',
        # 请求来源，本案例中其实是不需要加这个参数的，只是为了演示
        'referer': 'https://y.qq.com/n/yqq/song/004Z8Ihr0JIu5s.html',
        # 请求来源，携带的信息比“origin”更丰富，本案例中其实是不需要加这个参数的，只是为了演示
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        # 标记了请求从什么设备，什么浏览器上发出
    }
    # 伪装请求头
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'txt.yqq.song',
    'searchid':'70717568573156220',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(x+1),
    'n':'20',
    'w':name,
    'g_tk':'714057807',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'
    }
    # 将参数封装为字典
    music_info = []
    music_infoall = []
    music_infotatal = []
    res_music = requests.get(url,headers=headers,params=params)
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    for music in list_music:
        music_name = music['name']
        music_album = '所属专辑：'+music['album']['name']
        music_time = '播放时长：'+str(music['interval'])+'秒'
        music_url = 'https://y.qq.com/n/yqq/song/'+music['mid']+'.html'
        music_info = [music_name,music_album,music_time,music_url]
        sheet.append(music_info)
        print(music_info)
wb.save(name+'.xlsx')





