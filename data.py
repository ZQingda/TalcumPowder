from recordclass import recordclass

#Named Tuple for the Patient Data

PatientData = recordclass('PatientData', 'PatientID PatientName Condition Medicine Volume VolumeUnit Frequency FrequencyUnit DrugsTaken OtherDetails DoctorMessage')

ming = PatientData(PatientID='1208205005893863', PatientName='Ming', Condition='diabetes', Medicine='insulin', Volume=100, VolumeUnit='units per mL', Frequency='1', FrequencyUnit='Day', drugsTaken=0, OtherDetails='Eat before meals', DoctorMessage=" ")

michelle = PatientData('867521716617637', 'Ming', 'Anemia', 'Iron tablets', 2, 'pills', '2', 'Day', 0, 'none', ' ')

patients = [ming, michelle]

def getData(name):
    return patients[name]

def addPatient(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails):
    patient = PatientData(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails)
    patients.append(patient)
    return "You have been added to the database."

def resetDrugsTaken():
    for i in patients:
        i.DrugsTaken=0

doctorName = "Dr.Stein"

drugTaken = "Drug Taken"

invalidCommand = ":)"
