"""
    *微博抓取某个账号最新发布的微博内容并自动保存图片
    *示例ID：@央视频 - 7211561239
            @抖音短视频 - 6020086612
            @Youtube精选 - 2214257545
            @回形针PaperClip - 6414205745
"""
# -*- coding: utf-8 -*-
import urllib.request
import random, json, os, requests
import time

# url ="https://m.weibo.cn/api/container/getIndex?type=uid&value=6020086612&containerid=2315676020086612&page=1"

path = 'D:\\Code\\weibo\\'      # default video save path
id = '6020086612'               # default account(抖音短视频)
video_num = 0
weibo_name = "temp"             # default video save subfolder
header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
}
proxy_list = [
    {"http" : "58.58.213.55:8888"},
    {"http" : "218.249.45.162:35586"},
    {"http" : "59.110.243.174:8888"},
]
# proxy = {"http" : "58.58.213.55:8888"}

def use_proxy(url,proxy_addr):
    # 随机选择一个代理
    proxy = random.choice(proxy_list)
    # 使用选择的代理构建代理处理器对象
    httpproxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(httpproxy_handler)
    request = urllib.request.Request(url,headers=header)
    response = opener.open(request)
    data = response.read().decode('utf-8')
    return data

def get_containerid(url):
    proxy = random.choice(proxy_list)
    data=use_proxy(url,proxy)
    content=json.loads(data).get('data')
    for data in content.get('tabsInfo').get('tabs'):
        if(data.get('tab_type')=='video'):
            containerid=data.get('containerid')
    return containerid

def get_userInfo(id):
    global weibo_name
    url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
    proxy = random.choice(proxy_list)
    data=use_proxy(url,proxy)
    content=json.loads(data).get('data')
    profile_image_url=content.get('userInfo').get('profile_image_url')
    description=content.get('userInfo').get('description')
    profile_url=content.get('userInfo').get('profile_url')
    verified=content.get('userInfo').get('verified')
    guanzhu=content.get('userInfo').get('follow_count')
    name=content.get('userInfo').get('screen_name')
    fensi=content.get('userInfo').get('followers_count')
    gender=content.get('userInfo').get('gender')
    urank=content.get('userInfo').get('urank')
    print("微博昵称："+name+"\n"+"微博主页地址："+profile_url+"\n"+"微博头像地址："+profile_image_url+"\n"+"是否认证："+str(verified)+"\n"+"微博说明："+description+"\n"+"关注人数："+str(guanzhu)+"\n"+"粉丝数："+str(fensi)+"\n"+"性别："+gender+"\n"+"微博等级："+str(urank)+"\n")
    weibo_name = name

def get_video(id,file):
    global video_num
    i=1
    while i < 2:
        url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id
        weibo_url='https://m.weibo.cn/api/container/getIndex?type=uid&value='+id+'&containerid='+get_containerid(url)+'&page='+str(i)
        try:
            proxy = random.choice(proxy_list)
            data=use_proxy(weibo_url,proxy)
            content=json.loads(data).get('data')
            cards=content.get('cards')
            if(len(cards)>0):
                for j in range(len(cards)):
                    print("-----正在爬取第"+str(i)+"页，第"+str(j+1)+"条微博------")
                    card_type=cards[j].get('card_type')
                    if(card_type==89):
                        mblog=cards[j].get('mblog')
                        attitudes_count=mblog.get('attitudes_count')
                        comments_count=mblog.get('comments_count')
                        created_at=mblog.get('created_at')
                        reposts_count=mblog.get('reposts_count')
                        # scheme=cards[j].get('scheme')
                        page_info = mblog.get('page_info')
                        page_url = page_info.get('page_url')
                        content=page_info.get('content2')
                        print(content)
                        if page_info.get('type') == 'video':
                            media_info = page_info.get('media_info')
                            stream_url = media_info.get('stream_url')
                            video = requests.get(stream_url)
                            video_num += 1
                            f = open(path+weibo_name+'\\'+str(video_num)+ '.mp4', 'ab')  # 存储图片，多媒体文件需要参数b（二进制文件）
                            f.write(video.content)  # 多媒体存储content
                            f.close()
 
                        with open(file,'a',encoding='utf-8') as fh:
                            fh.write("----第"+str(i)+"页，第"+str(j+1)+"条微博视频----"+"\n")
                            fh.write("微博地址："+str(page_url)+"\n"+"发布时间："+str(created_at)+"\n"+"微博内容："+content+"\n"+"点赞数："+str(attitudes_count)+"\n"+"评论数："+str(comments_count)+"\n"+"转发数："+str(reposts_count)+"\n")
                i+=1
            else:
                break
        except Exception as e:
            print(e)
            pass

 
if __name__ == "__main__":
    id = input("输入抓取的微博账号ID：")

    get_userInfo(id)

    if os.path.isdir(path+weibo_name):
        pass
    else:
        os.mkdir(path+weibo_name)
    file = path+weibo_name+'\\'+weibo_name+".txt"
    
    get_video(id, file)