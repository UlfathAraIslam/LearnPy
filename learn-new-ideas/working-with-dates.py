from datetime import datetime

d = datetime.strptime("2026-10-18", "%Y-%m-%d")
print(d.date())
print(d.strftime("%Y-%m")) 
datetime.strptime("2026-02-30", "%Y-%m-%d")
