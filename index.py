from flask import Flask, request
import requests
import talk
import sched, time

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

    '''s = sched.scheduler(time.time, time.sleep)
    def send_spam(a='default'):
        reply(sender, time.time())

    def spam_cycler():
        send_spam()
        s.enter(2, 1, send_spam)
        s.enter(4, 1, send_spam)
        s.enter(6, 1, send_spam)
        s.run()
        send_spam()

    spam_cycler()'''

    reply(sender, talk.tester(message) + sender)
 
    return "ok"

s2 = sched.scheduler(time.time, time.sleep)
def cycleHandle(a='default'):
    reply(1445503462150740, time.time())

def cycle2(a='default'):
    reply(1445503462150740, time.time())
    reply(1445503462150740, "It's cycling!")
    s2.enter(4, 1, cycleHandle, argument=('',))
    s2.enter(4, 2, cycle2, argument=('',))
    s2.run()

cycle2()
 
 
if __name__ == '__main__':
    app.run(debug=True)
