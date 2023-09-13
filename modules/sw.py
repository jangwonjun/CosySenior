from urllib.request import urlopen
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
from modules.identify_email import Send_Email
from env import EMAIL
from apscheduler.schedulers.background import BackgroundScheduler


sched = BackgroundScheduler()

'''
경쟁률 실시간 분석기이지만, 시간이 없어서 겁나 비효율적으로 코딩을 하였습니다. 더군다나 Beautiful Soup를 처음써보는지라 그랬습니다.
기본적인 모듈정리와 identify_SMTP를 이용하여 제작하였습니다! 
대학 합격을 기원하며... 
'''

class univ_ratio:
    def __init__(self,server_message):
        self.server_message = server_message
                
        #진학사인경우 ssl 사용이 가능하지만, 유웨이는 프로토콜로 사용해야함. ssl 경고가 발새앟여 사용이 불가능함.
            
        gacheon_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10190361.html'
        gatalic_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10030221.html'
        gagede_sw = 'http://ratio.uwayapply.com/Sl5KMDpXJkpmJSY6Jkp6ZlRm'
        gist_sw = 'http://ratio.uwayapply.com/Sl5KMCYlckpeJSY6Jkp6ZlRm'
        unist_sw = 'http://ratio.uwayapply.com/Sl5KMCYlVzpKXiUmOiZKemZUZg=='
        dgist_sw = 'http://ratio.uwayapply.com/Sl5KMCYlclZKXiUmOiZKemZUZg=='
        kwang_sw = 'http://ratio.uwayapply.com/Sl5KTjlKZiUmOiZKemZUZg=='
        soongsil_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio11010301.html'
        hangyang_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio11640281.html'
        donguck_sw = 'https://addon.jinhakapply.com/RatioV1/RatioH/Ratio10550291.html'
            
        result = urlopen(gacheon_sw)
        result2 = urlopen(gatalic_sw)
        result3 = urlopen(gagede_sw)
        result4 = urlopen(gist_sw)
        result5 = urlopen(unist_sw)
        result6 = urlopen(dgist_sw)
        result7 = urlopen(kwang_sw)
        result8 = urlopen(soongsil_sw)
        result9 = urlopen(hangyang_sw)
        result10 = urlopen(donguck_sw)
        
        html = result.read()
        html2 = result2.read()
        html3 = result3.read()
        html4 = result4.read()
        html5 = result5.read()
        html6 = result6.read()
        html7 = result7.read()
        html8 = result8.read()
        html9 = result9.read()
        html10 = result10.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        soup2 = BeautifulSoup(html2, 'html.parser')
        soup3 = BeautifulSoup(html3, 'html.parser')
        soup4 = BeautifulSoup(html4, 'html.parser')
        soup5 = BeautifulSoup(html5, 'html.parser')
        soup6 = BeautifulSoup(html6, 'html.parser')
        soup7 = BeautifulSoup(html7, 'html.parser')
        soup8 = BeautifulSoup(html8, 'html.parser')
        soup9 = BeautifulSoup(html9, 'html.parser')
        soup10 = BeautifulSoup(html10, 'html.parser')
        
        temp = soup.find("table", {'class':'tableRatio2'})
        temp2 = soup2.find("table", {'class':'tableRatio3'})
        temp3 = soup3.find_all("tr", {'class':'trFieldValue'})
        temp4 = soup4.find_all("tr", {'class':'trFieldValue'})
        temp5 = soup5.find_all("table", {'name':'YogangStat'})
        temp6 = soup6.find_all("tr", {'class':'trFieldValue'})
        temp7 = soup7.find_all("tr", {'class':'trFieldValue'})
        temp8 = soup8.find_all("table", {'class':'tableRatio3'})
        temp9 = soup9.find_all("table", {'class':'tableRatio3'})
        temp10 = soup10.find_all("table",{'class':'tableRatio3'})
        
        data10 = []
        data9 = []
        data8 = []
        data7 = []
        data6 = []
        data5 = []
        data4 = []
        data3 = []
        data = []
        data2 = []
        
        for td in soup.find_all('td'):
            data.append(td.text.strip())
        for td in soup2.find_all('td'):
            data2.append(td.text.strip())
        for td in soup3.find_all('td'):
            data3.append(td.text.strip())
        for td in soup4.find_all('td'):
            data4.append(td.text.strip())
        for td in soup5.find_all('td'):
            data5.append(td.text.strip())
        for td in soup6.find_all('td'):
            data6.append(td.text.strip())
        for td in soup7.find_all('td'):
            data7.append(td.text.strip())
        for td in soup8.find_all('td'):
            data8.append(td.text.strip())
        for td in soup9.find_all('td'):
            data9.append(td.text.strip())
        for td in soup10.find_all('td'):
            data10.append(td.text.strip())
  
        
        gacheon = "가천대 AI/SW 전형 : " + str(data[1079]), "| 모집인원 "+ data[1080] +"명" + " | 실시간 지원자수 "+ data[1081]+"명"," | 실시간 경쟁률 " + data[1082]
        gatalic =  "가톨릭대 잠재능력우수자(면접전형) : " + str(data2[492]), "| 모집인원 "+ data2[493] +"명" + " | 실시간 지원자수 "+ data2[494]+"명"," | 실시간 경쟁률 " + data2[495]
        gagede = "서울과기대 인공지능응용학과 : " + str(data3[284]), "| 모집인원 "+ data3[285] +"명" + " | 실시간 지원자수 "+ data3[286]+"명"," | 실시간 경쟁률 " + data3[287]
        gist = "GIST 특기자전형 : " + str(data4[12]), "| 모집인원 "+ data4[13] +"명" + " | 실시간 지원자수 "+ data4[14]+"명"," | 실시간 경쟁률 " + data4[15]
        unist =  "UNIST 특기자전형 :  " +  " | 모집인원 "+ data5[7] +"명" + " | 실시간 지원자수 "+ data5[8]+"명"," | 실시간 경쟁률 " + data5[9]
        dgist = "DGIST  :  " + data6[12] +  " | 모집인원 "+ data6[13] +"명" + " | 실시간 지원자수 "+ data6[14]+"명"," | 실시간 경쟁률 " + data6[15]
        kwang = "광운대 특기자전형  : " + data7[280] +  " | 모집인원 "+ data7[281] +"명" + " | 실시간 지원자수 "+ data7[282]+"명"," | 실시간 경쟁률 " + data7[283]
        soongsil = "숭실대 특기자전형  : " + data8[728] +  " | 모집인원 "+ data8[729] +"명" + " | 실시간 지원자수 "+ data8[730]+"명"," | 실시간 경쟁률 " + data8[731]
        hangyang = "한양대 특기자전형  : " + data9[850] +  " | 모집인원 "+ data9[851] +"명" + " | 실시간 지원자수 "+ data9[852]+"명"," | 실시간 경쟁률 " + data9[853]
        donguck = "동국대 doream  : " + data10[286] +  " | 모집인원 "+ data10[287] +"명" + " | 실시간 지원자수 "+ data10[288]+"명"," | 실시간 경쟁률 " + data10[289]
        
        print(server_message)
        
        final_result2 = []
        send_final_result = []
        final_result = "\n".join([str(gacheon), str(gatalic), str(gagede), str(unist), str(dgist), str(kwang), str(soongsil), str(hangyang),str(donguck)])
        check_univ_ratio = [str(data[1082]),"가천대"],[str(data2[495]),"가톨릭대"], [str(data3[287]),"서울과기대"],[str(data4[15]),"GIST"],[str(data5[9]),"UNIST"],[str(data6[15]),"DGIST"],[str(data7[283]),"광운대"],[str(data8[731]),"숭실대"],[str(data9[853]),"한양대"],[str(data10[289]),"동국대"]
        check_univ_ratio = sorted(check_univ_ratio, key=lambda x: x[0],reverse=True)
        for i in range(len(check_univ_ratio)):
            final_result2.append(check_univ_ratio[i][1])
            #print(f"실시간 경쟁률 기준 학교 순위 : {check_univ_ratio[i][1]}")
            
        send_final_result = "\n".join(["실시간 경쟁률",str(final_result),"실시간 경쟁률 순위",str(final_result2)]) 
        
        print(send_final_result)
        print("successfully")
        
        Send_Email(EMAIL.SEND, str(send_final_result), "대학교 실시간 경쟁률")
        
        
        
        