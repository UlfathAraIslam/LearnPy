#7
'''
-Start with tasks = ['Buy groceries', 'Call doctor', 'Pay bills']
-insert(0,"Submit report")to add to the top in the task
-use remove("Call doctor)to delete by value
-print remaining tasks.upper() to convert to uppercase
-check tasks > 2
- if tasks > 2 Busy day ahead!'
-else otherwise print 'Light day!'
'''
tasks = ['Buy groceries', 'Call doctor', 'Pay bills']
tasks.insert(0,"Submit report")
tasks.remove("Call doctor")
print(tasks[0].upper())
print(tasks[1].upper())
print(tasks[2].upper())
if(len(tasks) > 2):
    print("Busy day ahead!")
else:
    print("Light day!")
