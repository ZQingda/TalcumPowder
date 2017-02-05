from recordclass import recordclass

#Named Tuple for the Patient Data

PatientData = recordclass('PatientData', 'PatientID PatientName Condition Medicine Volume VolumeUnit Frequency FrequencyUnit HasTakenDrug OtherDetails')

joe = PatientData(PatientID='1208205005893863', PatientName='Joe', Condition='Diabetes', Medicine='Insulin', Volume=100, VolumeUnit='units per mL', Frequency='1', FrequencyUnit='Day', HasTakenDrug=False, OtherDetails='Eat before meals')

patients = [joe]

def getData(name):
    return patients[name]

def addPatient(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails):
    patient = PatientData(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails)
    patients.append(patient)
    return "You have been added to the database."

doctorName = "Dr.Stein"

drugTaken = "Drug Taken"

invalidCommand = ":)"
