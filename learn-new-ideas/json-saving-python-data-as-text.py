import json
data = {"next_id": 2, "expenses": [{"id": 1, "amount": 850}]}
text = json.dumps(data) 
print(text)