# 독거노인통합관제시스템 CosySenior 

<div><h2>🖥 STACKS</h2>
  <div class="center">
    <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white">
    <img src="https://img.shields.io/badge/nginx-00FF80?style=for-the-badge&logo=nginx&logoColor=black">
    <img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"> 
    <img src="https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white"> <br>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"> 
    <img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"> 
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"> 
    <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
    <img src="https://img.shields.io/badge/fontawesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white">
  </div>
</div>

<div><h2>Function</h2>
  <table>
    <tr>
        <th>모닝콜/건강문자</th>
        <th>말동무 챗봇</th>
        <th>주변기기 연동설정</th>
        <th>긴급상황 SOS</th>
    </tr>
    <tr>
        <td>자연어처리 기반으로한 모닝콜전화/메세지를 <br> 예약한 시간에 자동으로 전송해줍니다.</td>
        <td>독거노인들을 위해서 말동무가 되어줄 <br> 자연어처리기반 Pytorch 챗봇입니다.</td>
        <td>Pyserial을 이용하여 Arduino 연동이 가능합니다<br>(다만, 아직은 프로토타입니다.)</td>
        <td>긴급상황이 발생하면 자동으로 <br> 호출해줍니다.</td>
    </tr>
  </table>
</div>

<div><h2>제작과정</h2></div>
  <div><h3>Pytorch기반 Kogpt2 자연어처리 챗봇</h3>
    <div>
      modules/ai.py 에서 코드를 확인하실 수 있습니다. <br>
      Env처리를 통하여 Pt파일을 Enum_Class로 처리하였습니다. <br>
    </div>
  </div>
  <div><h3>모닝콜/알림문자 시스템 구현</h3>
    <div>
      보통 문자서비스를 사용하려면 국내 통신업체(대항사)를 사용해야합니다. <br>
      대항사들은 보통 PHP, JavaScript, Java API을 이용하여 서비스를 제공합니다. <br>
      벡엔드 프레임워크가 Flask로 구축하여 파이썬 모듈로 기능을 확장하는게 좋겠다고 생각하여 Solution을 생각했습니다. <br>
      Twilio API을 이용하여 Python환경에서 문자/전화 기능을 구현하였습니다. <br>
    </div>
  </div>
  <div><h3>Twilio API</h3>
    <div>
      구글에서 많은 Twilio 문자에 대한 레퍼런스가 많지만 전화에 대한 레퍼런스는 없습니다. <br>
      처음에 어떻게 해야할지 고민했지만 Twilio 공식 Reference에 설명되어 있는것을 이용하여 구축하였습니다. <br>             
      moduels/client_call.py, moduels/client_message.py에서 코드를 참고하세요! <br>
    </div>
  </div>
  
<div><h2>Update Log</h2></div>
  <div>
      [1.0V] 말동무 챗봇과 주변기기 연동설정 UX가 수정되었습니다. <br>
      [1.1V] 모닝콜/건강문자 기능이 추가되었습니다. 긴급상황발생 기능을 추가하였습니다. 채널톡을 추가하였습니다. <br> 구글 통계를 추가하였습니다. ORM을 통한 회원가입/로그인 기능을 구축하였습니다. ORM을 통한 모닝콜/건강문          자 기능을 추가 및 수정하였습니다<br> 
      [1.2V] 서비스 안정화를 진행하였습니다. Pyserial을 통한 Arduino 연동 <br>
  </div>
