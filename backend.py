from flask import Flask, redirect, render_template, request
from datetime import timedelta, datetime
import os 

# The service exposes three APIs:
# `GET /<room>` Will return the static HTML (the provided front end), regardless of the room provided.
# `POST /api/chat/<room>`Accepts two form data fields - `username` and `message`.Will save date, time, username and message per room.
# `GET /api/chat/<room>` Returns the full chat in a room: Chat formatted as a list of `\n` delimited lines (1 per message)Each line formatted according to the example:
#"[2024-09-10 14:00:51] Roey: Hi everybody!"
#made by Yuval Dar & Daniel Zenkin
 
app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=1) # define app ttl
CHAT_FOLDER = 'chats'  # Directory to store chat files
os.makedirs(CHAT_FOLDER, exist_ok=True) #make chats folder if not there
# dictionary to store chat

# 1. A implemented by Daniel
@app.route("/")
def home():
	return render_template("index.html")

# 1. B implemented by Yuval
@app.route('/<room>', methods=['GET'])
def get_chat(room):
    # return chat for the room or an empty string if no messages exist
	return render_template("index.html")

#2. A implemented by Daniel
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat_history(room):
    #Returns the full chat in a room, newline delimited
    filename = os.path.join(CHAT_FOLDER, f'{room}.txt')
    try: # try to read file, if not exists will return empty
        with open(filename, 'r') as f:
            chat_history = f.read()
        return chat_history, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "", 200, {'Content-Type': 'text/plain'}
    
# 2. B implemented by Yuval
@app.route('/api/chat/<room>', methods=['POST'])
def post_chat(room):
    #function to add message and write it to a text file for storage
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

### MAIN #####
if __name__ == "__main__":
	app.run(debug=True)