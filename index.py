from flask import Flask, request
import requests
import talk
import sched, time
import threading
import data

app = Flask(__name__)
 
#ACCESS_TOKEN = "EAAQZB82BO6vQBAMPfxzKhVLneegYfihHOJh4GoTPJQoNLPe7hhjePY4TJGLSS4uMFQkFZAL0uB3NbsbA6aiSKZAh4QZCuVcOp7ZCK1nDMZCjgy9jcmcmowCse15PApLLsxuyBBHojZByF10NNp05eFJK9ZBNEeZCoJEmaqfvHoWtkswZDZD"
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
    data1 = request.json
    sender = data1['entry'][0]['messaging'][0]['sender']['id']
    message = data1['entry'][0]['messaging'][0]['message']['text']
    
    reply(sender, talk.tester(message, sender))
    if len(message) >= 14 and message[:14] == "Message Doctor":
        for i in data.patients:
            if i.PatientID == sender:
                reply(1445503462150740, i.PatientName + " : " + i.DoctorMessage)
    return "ok"

s2 = sched.scheduler(time.time, time.sleep)
def cycleHandle(a='default'):
    reply(1445503462150740, time.time())

def wakeupReminder(a='default'):
    #iterates through list of patients and reminds each
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "Wake up!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))

    #reply(1445503462150740, "Wake up!")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def morningReminder(a='default'):
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "Good morning!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))
 #iterates through list of patients and reminds each
    #reply(1445503462150740, "Good morning!")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def noonReminder(a='default'):
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "It's high noon!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))
#iterates through list of patients and reminds each
    #reply(1445503462150740, "It's high noon!")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def afternoonReminder(a='default'):
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "It is slightly past midday!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))
#iterates through list of patients and reminds each
    #reply(1445503462150740, "It's slightly past midday.")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def eveningReminder(a='default'):
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "Good evening!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))
#iterates through list of patients and reminds each
    #reply(1445503462150740, "Good evening!")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def nightReminder(a='default'):
    for i in data.patients:
        if i.PatientID != -1: #this would mean that a user is not properly set up yet
            if i.DrugsTaken < int(i.Frequency):
                reply(i.PatientID, "Sleep well!")
                reply(i.PatientID, talk.getReminder(i.PatientName, str(i.Volume) + " " + i.VolumeUnit + " of " + i.Medicine))
#iterates through list of patients and reminds each
    #reply(1445503462150740, "Good night!")
    #reply(1445503462150740, talk.getReminder("username", "dosage"))

def cycle2(a='default'):
    reply(1445503462150740, "It's cycling!")
    s2.enter(60, 1, wakeupReminder, argument=('',))
    s2.enter(120, 1, morningReminder, argument=('',))
    s2.enter(180, 1, noonReminder, argument=('',))
    s2.enter(240, 1, afternoonReminder, argument=('',))
    s2.enter(300, 1, eveningReminder, argument=('',))
    s2.enter(360, 1, nightReminder, argument=('',))
    s2.enter(420, 2, cycle2, argument=('',))
    data.resetDrugsTaken()
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

