from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'Anajana-i-love-her'

chat_msg = []

@app.route('/')
def entry():
    return render_template('login.html')

@app.route('/chat-screen', methods=['POST'])
def chat():
    naam = request.form.get('username')
    session['username'] = naam
    return render_template('index.html', user_name=naam, chat_messages=chat_msg)

@app.route('/message', methods=['POST'])
def msgs():
    txt = request.form.get('msg_input')
    naam = session.get('username')
    if txt:
        chat_msg.append({'nam': naam, 'msg': txt})
    return render_template('index.html', user_name=naam, chat_messages=chat_msg)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
