#Proxies Generator
#Github : X-blax
#Version : 1.0

from bs4 import BeautifulSoup as bs
import requests as rq
import random as rn
import os

os.system("clear")

n = "\033[m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
w = "\033[1;37m"
b = "\033[1;34m"
p = "\033[1;35m"
cy = "\033[1;36m"

colors = [r,g,y,w,b,p,cy]

headers = {'User-Agent' : 'Mozilla/5.0'}

r = rq.get("https://www.us-proxy.org/",headers=headers).text

s = bs(r,"html.parser")
hosts = s.find("textarea",{"class":"form-control"})

list = (hosts.text).split("\n")

for host in list:
    color = rn.choice(colors)
    if host == "":
        continue
    else:
        print(color+"[+]"+host+n)
