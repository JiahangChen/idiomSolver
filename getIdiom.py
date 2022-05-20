import requests, time, urllib.request, re
from moviepy.editor import *
import os, sys


def get_page(url_page):
    detail_page = requests.get(url_page).text
    list_find = re.findall('<li><a href=".+?html">(....)</a></li>', detail_page)
    return list_find



if __name__ == '__main__':
    allList = []
    for i in range(1,27):
        print(str(i) + " start")
        detail_page = requests.get("https://www.chengyucidian.net/letter/" + str(i) + "/p/1").text
        list_find = re.findall('<li ><a href=".+?p/.+?">(.+?)</a></li>',detail_page)
        for j in range(1, len(list_find) + 1):
            allList += get_page("https://www.chengyucidian.net/letter/" + str(i) + "/p/" + str(j))
    file = open("idiom_list.txt", 'w')
    for k in allList:
        file.write(k)
        file.write('\n')
    file.close()
