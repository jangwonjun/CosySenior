#define MQ2pin A0

float sensorValue;  //센서값 저장용 변수     
const int flamePin = 11;
int Flame = HIGH;


void setup()
{
  Serial.begin(9600); // 9600bps의 속도로 시리얼 통신 시작
  Serial.println("독거노인통합관제시스템 CosySenior");
  delay(10); 
  pinMode(flamePin, INPUT);
 
}

int detect_smoke(){ 
  sensorValue = analogRead(MQ2pin); // 아날로그 값을 읽어들

  Serial.print("센서입력: ");        //센서값 출력
  Serial.print(sensorValue);


  if(sensorValue > 300)          // 값이 300을 넘으면 
  {
    Serial.print("연기가 감지되었습니다! 확인이 필요합니다!");      //연기감지라고 표시하기
  }
  
  Serial.println("");
  delay(200); // 2초 후 다시 읽어들임    

}

int detect_flame(){
    Flame = digitalRead(flamePin);
    if (Flame== HIGH)
      {
        Serial.println("화재 발생 신속히 대피해주시길 바랍니다!");
      }
    else
    {
      Serial.println("이상 없음");
    }

}

void loop()
{
  
  detect_smoke();
  detect_flame();
  
}


