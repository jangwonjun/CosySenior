from flask import Flask, request, redirect, render_template, url_for
from urllib.parse import urlencode
from modules.orm import User
from modules.ai import WonJunAI
from modules.database import init_db
from env import FLASK_ENUM, AI_ENUM
from proctitle import setproctitle
import os
from modules.client_message import Sending
from modules.client_message import Client
# import config
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)


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
    if request.method == 'POST':
        user_name = request.form.get('user_name') 
        id = request.form.get('id')
        password = request.form.get('password') 
    else : 
        return render_template('register.html')

@app.route('/login')
def login():
    next = request.args.get('next', '')  # login 후 이동할 페이지 지정
    error_code = request.args.get('error_code', '')
    print(next, error_code)
    return render_template('login.html', next=next, error_code=error_code)

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
    if user.password == password:
        # login 한 사용자의 정보를 session에 저장해줌
        login_user(user)
        return redirect(safe_next_redirect)
    return redirect(url_for('login', next=next, error_code='password_incorrect'))


@app.route('/logout', methods=['GET'])
def logout():
    # flask login으로 logout >> 사용자 정보 세션 삭제
    logout_user()
    return redirect(url_for('home'))


@app.route('/messages', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        client_phone_number = request.form.get('phone_number') 
        reserve_day = request.form['timeInput']
    else : 
        return render_template('message.html')
    
@app.route('/arduino', methods=['GET', 'POST'])
def arduino():
    return render_template('arduino.html')

@app.route('/schedule', methods=['GET', 'POST'])
def schedule_master():
    return render_template('schedule.html')




if __name__ == '__main__':
    app.run('0.0.0.0', debug=FLASK_ENUM.DEBUG, port=FLASK_ENUM.PORT)

