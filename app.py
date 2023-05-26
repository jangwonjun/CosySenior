from flask import Flask, render_template, request
from modules.ai import WonJunAI
import env
from proctitle import setproctitle

setproctitle.setproctitle(env.PROC_NAME)

ai = WonJunAI(env.PT_ROUTE)
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


if __name__ == '__main__':
    app.run('0.0.0.0', debug=env.DEBUG, port=env.PORT)
