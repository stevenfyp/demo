import requests
from bs4 import BeautifulSoup
import time
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = ('张佳玮-知乎文章')
list = ['文章名称','文章简介','文章链接']
sheet.append(list)
headers={
    'origin':'https://www.zhihu.com/',
    'referer':'https://www.zhihu.com/people/zhang-jia-wei/posts/posts_by_votes',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url1 = 'https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles'
params = {
'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
'offset':'0',
'limit':'5',
'sort_by':'voteups'
}
# 将参数封装为字典
res1 = requests.get(url1,headers=headers,params=params)
res_json = res1.json()
json_titles = res_json['data']
x=0
for json_title in json_titles:
    x=x+1
    print('-----------------------打印第%s条------------------------' % x)
    json_name = json_title['title']
    json_url = json_title['url']
    json_content = json_title['excerpt'].replace('<b>','').replace('</b>','')
    list1 = [json_name,json_content,json_url]
    print('文章标题：'+json_name,'\n文章简要：'+json_content,'\n文章链接：'+json_url)
    time.sleep(2)
    sheet.append(list1)
wb.save('大V张佳玮.xlsx')
55555


# # 练习答案
# import requests
# headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# url='https://www.zhihu.com/api/v4/members/zhang-jia-wei/articles?'
# articlelist=[]
# #建立一个空列表，以待写入数据
# offset=0
# #设置offset的起始值为0
# while True:
#     params={
#         'include':'data[*].comment_count,suggest_edit,is_normal,thumbnail_extra_info,thumbnail,can_comment,comment_permission,admin_closed_comment,content,voteup_count,created,updated,upvoted_followees,voting,review_info,is_labeled,label_info;data[*].author.badge[?(type=best_answerer)].topics',
#         'offset':str(offset),
#         'limit':'20',
#         'sort_by':'voteups',
#         }
#     #封装参数
#     res=requests.get(url,headers=headers,params=params)
#     #发送请求，并把响应内容赋值到变量res里面
#     articles=res.json()
#     # print(articles)
#     data=articles['data']
#     #定位数据
#     for i in data:
#         list1=[i['title'],i['url'],i['excerpt']]
#         #把数据封装成列表
#         articlelist.append(list1)
#     offset=offset+20
#     #在while循环内部，offset的值每次增加20
#     if offset>40:
#         break
#     #如果offset大于40，即爬了两页，就停止
#     #if articles['paging']['is_end'] == True:
#     #如果键is_end所对应的值是True，就结束while循环。
#         #break
# print(articlelist)