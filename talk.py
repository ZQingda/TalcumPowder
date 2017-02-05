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
    return 'You have taken your medicine, {}, great!'.format(username)

def getIntro(username, doctorName, condition):
    return 'Hey {}! I am your medicine manager assigned by Dr.{}. You have been prescribed medicine for {}. You will be reminded by me to take your medicine at timed intervals your doctor has provided me. To list the details of this prescription, send <details>. For more information send <help>.'.format(username, doctorName, condition)

def getDetails(condition, dosage, interval):
    return 'Your have been prescribed medicine for {}. You will be taking {} {}. For details on how to take your medicine, send <details>.'.format(condition, dosage, interval)

def getReminder(username, dosage):
    return 'Hello {}! Reminder that you need to take {} now!'.format(username, dosage)
