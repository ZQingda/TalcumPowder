from recordclass import recordclass

#Named Tuple for the Patient Data

PatientData = recordclass('PatientData', 'PatientID PatientName Condition Medicine Volume VolumeUnit Frequency FrequencyUnit HasTakenDrug OtherDetails')

joe = PatientData(PatientID='1208205005893863', PatientName='Joe', Condition='diabetes', Medicine='insulin', Volume=100, VolumeUnit='units per mL', Frequency='1', FrequencyUnit='Day', HasTakenDrug=False, OtherDetails='Eat before meals')

esme = PatientData('867521716617637', 'Esme', 'chronic diarrhoea', 'bull testicle pills', 2, 'pills', 'once', 'day', False, 'none')

patients = [joe, esme]

def getData(name):
    return patients[name]

def addPatient(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails):
    patient = PatientData(id, name, condition, medicine, volume, volumeUnit, freq, freqUnit, hasTakenDrug, otherDetails)
    patients.append(patient)
    return "You have been added to the database."

doctorName = "Dr.Stein"

drugTaken = "Drug Taken"

invalidCommand = ":)"
