from flask import Flask, redirect, render_template, request
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=1)

# dictionary to store chat
chats = {}

# implemented by Danielle
@app.route("/")
def home():
	return render_template("index.html")

# implemented by Yuval
@app.route('/api/chat/<room>', methods=['GET'])
def get_chat(room):
    # return chat for the room or an empty string if no messages exist
    return "\n".join(chats.get(room, []))




if __name__ == "__main__":
	app.run(debug=True)