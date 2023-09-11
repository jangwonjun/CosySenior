from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser

class univ_ratio:
    def __init__(self,time):
        self.time = time
        gacheon_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10190361.html'
        gatalic_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10030221.html'
        
        result = urlopen(gacheon_sw)
        result2 = urlopen(gatalic_sw)
        
        html = result.read()
        html2 = result2.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        soup2 = BeautifulSoup(html2, 'html.parser')
        
        temp = soup.find("table", {'class':'tableRatio2'})
        temp2 = soup2.find("table", {'class':'tableRatio3'})
        
        data = []
        data2 = []
        
        for td in soup.find_all('td'):
            data.append(td.text.strip())
        for td in soup2.find_all('td'):
            data2.append(td.text.strip())
            
        print(time)
        print("가천대 AI/SW 전형 : " + str(data[1079]), "| 모집인원 "+ data[1080] +"명" + " | 실시간 지원자수 "+ data[1081]+"명"," | 실시간 경쟁률 " + data[1082])
        print("가톨릭대 잠재능력우수자(면접전형) : " + str(data2[492]), "| 모집인원 "+ data2[493] +"명" + " | 실시간 지원자수 "+ data2[494]+"명"," | 실시간 경쟁률 " + data2[495])
        print("scuccessfully")
        print(result)
        