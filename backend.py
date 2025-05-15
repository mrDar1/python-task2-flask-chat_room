from flask import Flask, redirect, render_template, request
from datetime import timedelta, datetime
import os 

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=1)
CHAT_FOLDER = 'chats'  # Directory to store chat files
os.makedirs(CHAT_FOLDER, exist_ok=True)
# dictionary to store chat

# implemented by Daniel
@app.route("/")
def home():
	return render_template("index.html")

# implemented by Yuvalb
@app.route('/<room>', methods=['GET'])
def get_chat(room):
    # return chat for the room or an empty string if no messages exist
    # return "\n".join(chats.get(room, [])) # fail option
	return render_template("index.html")
	
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat_history(room):
    #Returns the full chat in a room, newline delimited
    filename = os.path.join(CHAT_FOLDER, f'{room}.txt')
    try:
        with open(filename, 'r') as f:
            chat_history = f.read()
        return chat_history, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "", 200, {'Content-Type': 'text/plain'}
    

@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    username = request.form.get('username')
    msg = request.form.get('msg')

    if not username or not msg:
        return "miss username or message", 400

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    filename = os.path.join(CHAT_FOLDER, f'{room}.txt')

    try:
        with open(filename, 'a') as f:
            # append timestamp, username, msg
            f.write(f"[{timestamp}] {username}: {msg}\n")
    except FileNotFoundError:
        return "fail open file", 500

    return "success", 200  # Returning plain string


if __name__ == "__main__":
	app.run(debug=True)