import collections

#Named Tuple for the Patient Data

PatientData = collections.namedtuple('PatientData', 'PatientID PatientName Condition Medicine Volume VolumeUnit Frequency FrequencyUnit OtherDetails')

joe = PatientData(PatientID='1208205005893863', PatientName='joe', Condition='Diabetes', Medicine='Insulin', Volume=100, VolumeUnit='units per mL', Frequency='1', FrequencyUnit='Day', OtherDetails='Eat before meals')

def tester(say):
    return "How about this!"
