#1
#Write a Python program to subtract five days from current date.
from datetime import date,timedelta
today=date.today()
five=today-timedelta(5)
print(five)

#2
#Write a Python program to print yesterday, today, tomorrow.
from datetime import date,timedelta
today=date.today()
yesterday=today-timedelta(1)
tomorrow=today+timedelta(1)
print(yesterday)
print(today)
print(tomorrow)

#3
#Write a Python program to drop microseconds from datetime.
from datetime import datetime
date=datetime.now()
dates=date.replace(microsecond=0)
print(dates)

#4
#Write a Python program to calculate two date difference in seconds.
from datetime import datetime
today=date.today()
yesterday=today-timedelta(1)
difereence=today-yesterday
print(difereence.total_seconds())