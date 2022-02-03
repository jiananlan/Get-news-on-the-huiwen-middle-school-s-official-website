#!/usr/bin/env python
#-*-coding:utf-8-*-
import urllib
import urllib.request
from time import sleep
from random import randint
import re
import winsound


def getPage(url):
    request  = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    #sleep(randint(0,2))
    return response.read().decode("utf-8", "ignore")

def pageerror(url):
    try:
        getPage(url)
    except:
        return 0
    return 1
i=1
while pageerror('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/c6c7c01e-'+str(i)+'.html')!=0:
    i=i+1
#获取总页面数

i=i-1
#i=146
print(i)
'''rgg=['http://www.huiwen.edu.cn/hwmh/xw74/qbxw/qt64/227901/index.html']
rgg.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/ys/227898/index.html')
rgg.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/qt64/227858/index.html')
rgg.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/jx/227855/index.html')
rgg.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/jx/227852/index.html')'''
black=['version', '/hwmh/uiFramework/huilan-jquery-ui/css/huilan-jquery-ui.css', '></script>\n <meta name=', 'code-YBXiJRUJW0', '/hwmh/template/hwmh.css?timestamp=1606439370926', '/hwmh/template/page/list/skin.css?timestamp=1606439370926', '2', '/hwmh/uiFramework/commonResource/css/bootstrap.css', 'sg-top-nav', 'collapse navbar-collapse', '/hwmh/gk/xxjj21/index.html', '/hwmh/xw74/qbxw/index.html', '/hwmh/kc/qbkc/index.html', '/hwmh/js/jsgk/index.html', '/hwmh/index/index.html', '/hwmh/dj/djgk/index.html', '/hwmh/zs23/zsgk/index.html', '/hwmh/xy/hwxyml/index.html', '/hwmh/zp57/hyjr/index.html', '/eportal/ui?pageId=212431', '/eportal/ui?pageId=212817', '/eportal/ui?pageId=212848', '/eportal/ui?pageId=212888', '/eportal/ui?pageId=212558', '/eportal/ui?pageId=212927', '/eportal/ui?pageId=212937', '/eportal/ui?pageId=213081', '/eportal/ui?pageId=213090', 'sg-top-image-container', '/hwmh/uiFramework/commonResource/css/bootstrap.css', '/hwmh/uiFramework/commonResource/css/all.min.css', 'top: 53.85px;', '535c2f4d8d99434791b682ae8c90e04a', 'portlet-header', 'shadow dn', 'sg-category-title', '/hwmh/xw74/qbxw/index.html', '/hwmh/xw74/qbxw/dj65/index.html', '/hwmh/xw74/qbxw/td/index.html', '/hwmh/xw74/qbxw/gh/index.html', '/hwmh/xw74/qbxw/jx/index.html', '/hwmh/xw74/qbxw/jky12/index.html', '/hwmh/xw74/qbxw/dy37/index.html', '/hwmh/xw74/qbxw/ys/index.html', '/hwmh/xw74/qbxw/ty13/index.html', '/hwmh/xw74/qbxw/kj58/index.html', '/hwmh/xw74/qbxw/gjb/index.html', '/hwmh/xw74/qbxw/dwjl52/index.html', '/hwmh/xw74/qbxw/qt64/index.html', '/hwmh/xw74/qbxw/220964/index.html', '/hwmh/xw74/qbxw/222615/index.html', 'sg-news-detail-box sg-article-detail-box', 'left', 'sg-news-list', '/hwmh/xw74/qbxw/qt64/227901/index.html', 'sg-item-box', '/hwmh/xw74/qbxw/ys/227898/index.html', 'sg-item-box', '/hwmh/xw74/qbxw/qt64/227858/index.html', 'sg-item-box', '/hwmh/xw74/qbxw/jx/227855/index.html', 'sg-item-box', '/hwmh/xw74/qbxw/jx/227852/index.html', 'sg-item-box', 'NormalRed', 'width:5px;display:inline-block;', 'sg-footer-info-container', 'sg-icon-box', 'sg-quick-info-title', 'sg-quick-info-item', '/hwmh/gk/xxjj21/index.html', '/hwmh/gk/bnxs/index.html', '/hwmh/gk/lxwm48/index.html', 'sg-quick-info-title', 'sg-quick-info-item', '/hwmh/kc/qbkc/msjt/index.html', '/hwmh/kc/qbkc/sjkc/index.html', '/hwmh/kc/qbkc/tskc25/index.html', '/hwmh/kc/qbkc/xxkc5/index.html', 'sg-quick-info-title', 'sg-quick-info-item', '/hwmh/zs23/zsgk/zsjz79/index.html', '/hwmh/zs23/zsgk/gjbzs-english/index.html', '/hwmh/zs23/zsgk/gjbzs-korean/index.html', 'sg-quick-info-title', 'sg-quick-info-item', '/hwmh/zs23/zpgw/index.html', 'container', 'http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003641', 'https://beian.miit.gov.cn', '.sg-article-breadcrumb', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ', '.sg-nav-item ']


got=getPage('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/c6c7c01e-1.html')



collect=''
d=0
#The code below can bee used as a refresh way to get unuseable url(s).

'''
for x in got:
         if x=='f' and d==0:
                  d=1
         if x=='=' and d==1:
                  d=2
         if x=='"' and d==2:
                  d=3
         elif x=='"' and d==3:
                  d=0
                  collect=collect.replace('"','')
                  if collect not in rgg:
                      black.append(collect)
                  collect=''
         if d==3:
                  collect=collect+x

print(black)'''

d=0
rgg=[]
for v in range(i-1):
    d1=getPage('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/c6c7c01e-'+str(v+1)+'.html')
    #for x in d1:
        
    for x in d1:
         if x=='f' and d==0:
                  d=1
         if x=='=' and d==1:
                  d=2
         if x=='"' and d==2:
                  d=3
         elif x=='"' and d==3:
                  d=0
                  collect=collect.replace('"','')
                  if collect not in black:
                      rgg.append(collect)
                  collect=''
         if d==3:
                  collect=collect+x
print('_________')
print(rgg)



def getit(url):
    #url = 'http://www.huiwen.edu.cn/hwmh/xw74/qbxw/qt64/227901/index.html'
    #f=open('all.txt',mode='w+')
    try:
        p=getPage(url)
        #print(p)
    except:
        #print('ERROR')
        return 'Error'
    tt=[]
    #yy=[]
    collect=''
    for x in p:
        if x=='<':
            #collect=''
            collect=x
        elif x=='>':
            collect=collect+x
            if (collect) in tt:
                collect=''
                continue
            else:
                tt.append(collect)
                #yy.append(collect)
        else:
            collect=collect+x
    #f.writelines(tt)
    #f.close          .easysite-body
    #print(tt)
    for x in tt:
        p=p.replace(x,'')
    z='&nbsp; '
    c=len(z)
    collect=''
    get=''
    d=0
    for x in p:
        if x=='原':
            collect=x
        if x=='文' and collect=='原':
            d=1
        #if x
        if d==1 and x=='e':
            collect='e'
        if d==1 and x=='a' and collect=='e':
            d=0

        
        if d==1:
            get=get+x
    #print(p)  .e

    get=get.replace(z,'_')
    get=get.replace(' ','')
    get=get.replace('.e','')
    get=get.replace('文','')
    return get

def getimg(url):
    html=getPage(url)
    imgre=re.compile(r'src="(.*?)"class=')
    imglist=re.findall(imgre.html)
#f.writelines(tt)
#rr=['http://www.huiwen.edu.cn/hwmh/xw74/qbxw/qt64/227901/index.html']
#rr.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/ys/227898/index.html')
#rr.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/qt64/227858/index.html')
#rr.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/jx/227855/index.html')
#rr.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/jx/227852/index.html')
#rr.append('http://www.huiwen.edu.cn/hwmh/xw74/qbxw/jx/213915/index.html')
for x in rgg:
    print(getit('http://www.huiwen.edu.cn'+x))
    print('>>>')

print()

