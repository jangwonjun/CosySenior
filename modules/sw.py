from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser

class univ_ratio:
    def __init__(self,time):
        self.time = time
        gacheon_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10190361.html'
        result = urlopen(gacheon_sw)
        html = result.read()
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find("table", {'class':'tableRatio2'})
        data = []
        for td in soup.find_all('td'):
            data.append(td.text.strip())

        print(time)
        result = "전형 이름 : " + str(data[27]), "| 모집인원 "+ data[28] +"명" + " | 실시간 지원자수 "+ data[29]+"명"," | 실시간 경쟁률 " + data[30]
        print("scuccessfully")
        print(result)