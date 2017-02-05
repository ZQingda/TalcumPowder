from flask import Flask, request
import requests
import talk
import sched, time
import threading

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
    s2.enter(300, 1, cycleHandle, argument=('',))
    s2.enter(300, 2, cycle2, argument=('',))
    s2.run()

'''cycle2()'''
def appRun():
    app.run(debug=False)

class appThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      appRun()
      print ("Exiting " + self.name)

class spamThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print ("Starting " + self.name)
      cycle2()
      print ("Exiting " + self.name)

thread1 = appThread(1, "Thread-App", 1)
thread2 = spamThread(2, "Thread-Spam", 2)

thread1.start()
thread2.start()
 
''' 
if __name__ == '__main__':
    app.run(debug=True)'''

