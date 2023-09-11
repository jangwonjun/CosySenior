from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
import time
from flask import Flask, request, redirect, render_template, url_for
from urllib.parse import urlencode
from modules.orm import User, CallLog
from modules.ai import WonJunAI
from modules.database import init_db
from env import FLASK_ENUM, AI_ENUM, CALL
from proctitle import setproctitle
import os
from modules.client_message import Sending
from modules.client_call import Calling
from apscheduler.schedulers.background import BackgroundScheduler
from modules.identify_email import Send_Email
from modules.sw import univ_ratio
sched = BackgroundScheduler()
caller = Calling()
Sender = Sending()
# from modules.arduino import measure_arduino


setproctitle.setproctitle(FLASK_ENUM.PROC_NAME)

ai = WonJunAI(AI_ENUM.PT_ROUTE)
app = Flask(__name__, static_url_path='/static')
app.secret_key = FLASK_ENUM.SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

init_db()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.unauthorized_handler
def unauthorized_callback():
    # print(dir(request))
    # login이 필요한 page에 접근 시 login page로 이동을 시켜줌
    query_string = urlencode(request.args)

    return redirect(url_for('login', next=f'{request.path}?{query_string}'))


@app.route('/')
@login_required
def home():
    user = current_user
    return render_template('index.html', user=user)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    try:
        text = request.get_json()
        if value := text.get('text'):
            value = ai.create_response(value)
            return {'text': value}
    except Exception as e:
        print(e)
        return render_template('chatbot.html', title='CosySenior')


@app.route('/voice_control', methods=['GET', 'POST'])
def voicechat():
    return render_template('aichat.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup_method():
    if request.method != 'POST':
        return render_template('register.html')
    name: str = request.form.get('name')
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    phone_number: str = request.form.get('phoneNumber')
    help_phone_number: str = request.form.get('helperPhoneNumber')
    phone_number = phone_number.replace("-", "")
    help_phone_number = help_phone_number.replace("-", "")
    if phone_number.startswith('010'):
        phone_number = "+8210" + phone_number[3:]
    if help_phone_number.startswith('010'):
        help_phone_number = "+8210" + help_phone_number[3:]

    if (email.find('@') == -1):
        return render_template('register.html')

    user = User.create(email, password, name,
                       phone_number, help_phone_number)
    return redirect(url_for('login', next=next, status_code='account_created'))


@app.route('/login')
def login():
    next = request.args.get('next', '')  # login 후 이동할 페이지 지정
    status_code = request.args.get('status_code', '')
    return render_template('login.html', next=next, status_code=status_code)


@app.route('/login/auth', methods=['POST'])
def login_auth():
    # form 방식으로 받아올 때에는 form에, json 방식으로 받아올 때에는 json에 원하는 정보가 담겨있음
    email = request.form.get('email')
    password = request.form.get('password')
    next = request.form.get('next')
    print(email, password, next)
    safe_next_redirect = url_for('home')
    if next:
        safe_next_redirect = next
    user = User.find_id_by_email(email)
    if user and user.password == password:
        # login 한 사용자의 정보를 session에 저장해줌
        login_user(user)
        return redirect(safe_next_redirect)
    return redirect(url_for('login', next=next, status_code='password_incorrect'))


@app.route('/logout', methods=['GET'])
def logout():
    # flask login으로 logout >> 사용자 정보 세션 삭제
    logout_user()
    return redirect(url_for('home'))


@app.route('/messages', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        time_value = request.form['time_input']
        CallLog.create(current_user.id, time_value)
    return render_template('message.html')


@app.route('/arduino', methods=['GET', 'POST'])
def arduino():
    try:
        measure_arduino()
    except Exception as e:
        print(e)
        return render_template('arduino.html', title='CosySenior')


@app.route('/emergency', methods=['GET', 'POST'])
def schedule_master():
    return render_template('schedule.html')

@app.route('/emailjang',methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        message_target = request.form['target'] #상대방
        message_title = request.form['title'] #제목
        message_context = request.form['msg'] #내용
        send_password = request.form['password'] #메세지 전송내용
        
        if send_password == CALL.PASSWORD:
            Send_Email(message_target, message_context, message_title)
    return render_template('email.html')

@app.route('/messagejang',methods=['GET', 'POST'])
def send_static_message():
    if request.method == 'POST':
        message_target = request.form['target'] #상대방 전화번호
        message_context = request.form['msg'] #메세지 전송내용
        send_password = request.form['password'] #메세지 전송내용
        
        if message_target.startswith('010'):
            message_target = "+8210" + message_target[3:]
                
        print(message_target,message_context,send_password)
        
        if send_password == CALL.PASSWORD:
            Sender.create_message(message_context, message_target)
            print("Successfully Messaging")
    #sender.create_message(message_target, message_context)
    
    return render_template('static_message.html')

@app.route('/calljang',methods=['GET', 'POST'])
def send_static_call():
    if request.method == 'POST':
        message_target = request.form['target'] #상대방 전화번호
        message_context = request.form['msg'] #메세지 전송내용
        send_password = request.form['password'] #메세지 전송내용
        
        if message_target.startswith('010'):
            message_target = "+8210" + message_target[3:]
                
        print(message_target,message_context,send_password)
        
        if send_password == CALL.PASSWORD:
            #caller.create_call(message_context, message_target)
            status_system = 1 
            return status_system
            print("Successfully Calling")
            
    return render_template('static_call.html')



@app.route('/test1')
def test_email():
    return render_template('lowyal.html')


@sched.scheduled_job('cron', second='10', id='send_message')
def send_message():
    current_time = time.strftime("%H:%M:00")
    #print(f"시작 시간: {current_time}")
    calls = CallLog.get_phone_by_call_time(current_time)
    #print(f"전화 리스트: {calls}")
    for call in calls:
        print(f"{call}에게 전화 시작")
        print(f"메세지: {ai.create_response('안녕')}")
        caller.create_call(ai.create_response("굿모닝"), to=call)
        sender.create_message(ai.create_response("활기찬 아침"), to=call)
        print("successful")

@sched.scheduled_job('cron', second='0', id='univ_ratio_check')
def univ_ratio_check():
    current_time = time.strftime("%H:%M:00")
    print(current_time)
    univ_ratio("대학경쟁률 실시간 조회")
    

sched.start()


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True, port=FLASK_ENUM.PORT)
