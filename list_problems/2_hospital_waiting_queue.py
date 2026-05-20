#2
'''
-Start with a pre-defined patient queue: ['Rin', 'Sam', 'Yuki']
-Use append() to add Leo.
-Use pop(0)to call and remove the first patient 'Rin' 
-Store the removed name
-print removed name in a sentence.
-print updated list
-use len() to count waiting patient and print it
'''

patient_queue = ['Rin', 'Sam', 'Yuki']
patient_queue.append("Leo")
first_calling_patient = patient_queue.pop(0)
print("Now calling:",first_calling_patient)
print("Remaining queue:", patient_queue)
print("Patients waiting:",len(patient_queue))