from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ai_chating')
def aichat():
    return render_template('templates/chatbot.html')

@app.route('/voice_order')
def voice_order():
    return render_template('voice_order.html')

if __name__ == '__main__':
    app.run(debug=True)
