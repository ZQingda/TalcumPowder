from flask import Flask, request
import requests
import talk
 
app = Flask(__name__)
 
ACCESS_TOKEN = "EAAITqsZBZAlFoBADKkz3kbZCjce9tcsZB93BRbifwCozsQqHLlO4OBmRnBWZBU9kzYScXivOeoO5A5yJjYMlPZAraZBHfa9AL6An7cOxApqGEfEjmRk8q9lD769S9gtI0WGHzBER94awX1g4pepPDjEkm8GiZBzaxcpfHrFJRQQw8QZDZD"
 
 
def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)
 
 
@app.route('/', methods=['POST'])
def handle_incoming_messages():
    data = request.json
    sender = data['entry'][0]['messaging'][0]['sender']['id']
    message = data['entry'][0]['messaging'][0]['message']['text']
    reply(sender, talk.tester(message) + sender)
 
    return "ok"
 
 
if __name__ == '__main__':
    app.run(debug=True)
