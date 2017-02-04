import collections

#Named Tuple for the Patient Data

PatientData = collections.namedtuple('PatientData', 'PatientID PatientName Condition Medicine Volume VolumeUnit Frequency FrequencyUnit OtherDetails')

joe = PatientData(PatientID='1208205005893863', PatientName='joe', Condition='Diabetes', Medicine='Insulin', Volume=100, VolumeUnit='units per mL', Frequency='1', FrequencyUnit='Day', OtherDetails='Eat before meals')

PatientArray = [joe]

def tester(say):
    return "How about this!"

def getIntro(username, doctorName, condition):
    return 'Hey {}! I am your medicine manager assigned by Dr.{}. You have been prescribed medicine for {}. You will be reminded by me to take your medicine at timed intervals your doctor has provided me. To list the details of this prescription, send <details>. For more information send <help>.'.format(username, doctorName, condition)

def getDetails(condition, dosage, interval):
    return 'Your have been prescribed medicine for {}. You will be taking {} {}. For details on how to take your medicine, send <details>.'.format(condition, dosage, interval)

def getReminder(username, dosage):
    return 'Hello {}! Reminder that you need to take {} now!'.format(username, dosage)