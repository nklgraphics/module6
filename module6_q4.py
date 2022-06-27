from datetime import datetime

#current date
datetime_object = datetime.now()

#define feet, inches, date
def fid (f,i,d):
    print (f,"feet")
    print (i,"inches")
    print ("date", datetime_object)

f= input("Enter feet measurement")
i= input("Enter inches measurement")
d= datetime_object


