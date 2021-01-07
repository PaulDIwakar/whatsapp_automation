import pywhatkit 
print("ONLY FOR INDIA")
#input number
while True:
    try:
        num = input("Enter Number : ")
        if len(num) == 10:
            print("Number accepted")    
            break
        else:
            print("Number should be in 10 digit")
    except ValueError:
        print("check your number")
        continue
#input message
message = input("Type message : ")
print("Enter railway time")
#current time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
#input hour
while True:
    try:
        h = int(input("Enter hour : "))
        if h <= 24:
            print("hour added")
            break
        else:
            print("hour should be less than 24")
    except ValueError:
        print ("provide an integer value")
        continue
#input minute
while True:
    try:
        m = int(input("Enter minute : "))
        if m < 60:
            print("minute added")
            break
        else:
            print("Minute should be less than 60")
    except ValueError:
        print("provide an integer value")
        continue
#main
pywhatkit.sendwhatmsg("+91"+num,message, h, m)