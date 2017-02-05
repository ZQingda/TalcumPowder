import data

def tester(say):
    #check if id exists in the db array
    for i in data.patients:
        if i.PatientID == -1:
            return getIntro(i.PatientName, data.doctorName, i.Condition)
    #if the id doesn't exist, give the getIntro
        elif i.PatientID != -1:
    #if the id exists, look at the "say"
            if say == data.drugTaken:
                i.HasTakenDrug=True
                return 
            elif say == "Details":
                return getDetails(i.Condition, i.Volume + " " + i.VolumeUnit, i.Frequency + " " + i.FrequencyUnit)
        else:
            return data.invalidCommand
    
    #turn "drugTaken" into "true" 
    #get getDetails if asked for Detailed
    #else turn into "invalid command, try again" 
    return ":) :)!"

    
def tester(say):
    return "How about this! " + say + " "

def getHasTakenDrug(username):
    return 'You have taken your medicine, %s, great!' % (username)

def getIntro(username, doctorName, condition):
    return 'Hey %s! I am your medicine manager assigned by Dr.%s. You have been prescribed medicine for %s. You will be reminded by me to take your medicine at timed intervals your doctor has provided me. To list the details of this prescription, send <details>. For more information send <help>.' % s(username, doctorName, condition)

def getDetails(condition, dosage, interval):
    return 'Your have been prescribed medicine for %s. You will be taking %s %s. For details on how to take your medicine, send <details>.' % (condition, dosage, interval)

def getReminder(username, dosage):
    return 'Hello %s! Reminder that you need to take %s now!' % (username, dosage)
