# Ques 4. Extract day from the time.

from datetime import datetime

d= datetime.now()
print(d)
print("day:",d.strftime("%A"))
