import data

def tester(say, senderID):
    #check if id exists in the db array

    for i in data.patients:
        if i.PatientID == senderID:
            if say == data.drugTaken:
                i.HasTakenDrug=True
                return getHasTakenDrug(i.PatientName)
            elif say == "Details":
                return getDetails(i.Condition, str(i.Volume) + " " + i.VolumeUnit, str(i.Frequency) + " " + i.FrequencyUnit)
            else:
                 return "Sorry, I didn't catch that. \n To log a drug taken, type \"Drug Taken\". For more details, type \"Details\" :)"
    #turn "drugTaken" into "true" 
    #get getDetails if asked for Detailed
    #else turn into "invalid command, try again" 
    return "Hey new guy. Useless." #getIntroNew(" ")
    
#def tester(say):
#    return "How about this! " + say + " "

def getIntroNew(useless):
    return 'Hey! I am your medicine Manager, assigned by Dr. %s. I see that you are new here! Please talk to the Doctor to get a prescription.'% (data.doctorName)

def getHasTakenDrug(username):
    return 'You have taken your medicine, %s, great!' % (username)

def getIntro(username, doctorName, condition):
    return 'Hey %s! I am your medicine manager assigned by Dr.%s. You have been prescribed medicine for %s. You will be reminded by me to take your medicine at timed intervals your doctor has provided me. To list the details of this prescription, send "Details".' % (username, doctorName, condition)

def getDetails(condition, dosage, interval):
    return 'Your have been prescribed medicine for %s. You will be taking %s %s.' % (condition, dosage, interval)

def getReminder(username, dosage):
    return 'Hello %s! Reminder that you need to take %s now!' % (username, dosage)
