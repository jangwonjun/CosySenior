from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
from modules.identify_email import Send_Email
from env import EMAIL
from apscheduler.schedulers.background import BackgroundScheduler



class univ_ratio_2:
    def __init__(self,server_message):
        self.server_message = server_message
        busan_teach = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio20040171.html'

        result11 = urlopen(busan_teach)
        
        html11 = result11.read()
        
        soup11 = BeautifulSoup(html11, 'html.parser')
        
        temp11 = soup11.find_all("table", {'class':'tableRatio2'})
        
        
        data11 = []
        
        for td in soup11.find_all('td'):
            data11.append(td.text.strip())
        
        print(data11[16],data11[17],data11[18],data11[19])
        
        print(server_message)
        
        busan = "부산교육대학교  : " + data11[16] +  " | 모집인원 "+ data11[17] +"명" + " | 실시간 지원자수 "+ data11[18]+"명"," | 실시간 경쟁률 " + data11[19]
        
        Send_Email(EMAIL.SEND_2, str(busan), "부산교육대학교 실시간 경쟁률")