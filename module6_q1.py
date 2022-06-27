import sys
#import datetime, time, date
from datetime import datetime
from datetime import time
from datetime import date

#define functions
def main():
    dt = datetime.now()
   #utc = datetime.utcnow()
    time_string = dt.strftime("%X")
 

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) == 6:
            _date, _time, store, item, cost, payment = data
            print ("{dt}\t{time_string}\t{store}\t{item}\t{cost}\t{payment}")
main()

