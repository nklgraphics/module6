from datetime import datetime
from datetime import timedelta  

#add 1 day  
print(datetime.now()+timedelta(days=1))

#subtract 60 seconds
print(datetime.now()-timedelta(seconds=60))

#add 2 years
print(datetime.now()+timedelta(days=730))

