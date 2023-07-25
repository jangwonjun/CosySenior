from flask import Flask, render_template, request
from modules.ai import WonJunAI
from env import FLASK_ENUM
from proctitle import setproctitle
import os
from modules.client_message import Sending
from modules.client_message import Client
import config



setproctitle.setproctitle(FLASK_ENUM.PROC_NAME)

ai = WonJunAI(FLASK_ENUM.PT_ROUTE)
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def home():
    return render_template('index.html')


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

@app.route('/login', methods=['GET', 'POST'])
def login_method():
    if request.method == 'POST':
        user_name = request.form.get('user_name') 
        id = request.form.get('id')
        password = request.form.get('password') 
    else : 
        return render_template('login.html')

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
