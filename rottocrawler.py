# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


def get_ball_number(num1, num2):
    
    url1 = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo='
    lst = []
    for count in range(num1, num2):
        print("-------------%d-------------" % (count))
        url = url1 + str(count)
        url_p = requests.get(url)
        soup = BeautifulSoup(url_p.content, 'html.parser')
        
        temp_lst = []
        for ball in range(7):
            temp_lst.append(soup.select('.ball_645')[ball].get_text())
        
        tpl = tuple(temp_lst)
        lst.append(tpl)

    return lst

    
if __name__=="__main__":
    t_balls = get_ball_number(1, 4)
    for t in t_balls:
        print(t)
