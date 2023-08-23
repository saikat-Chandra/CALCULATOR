#USING IF ELSE MAKING A TIME ZONE SAY GOOD MORNINH , AFTERNOON , EVENING , & NIGHT
import time
s=input("Please Enter Your Name")
timemonitaring=time.strftime('%H:%M:%S')
print(timemonitaring)
timemonitaring=time.strftime('%H')
print(timemonitaring)
timemonitaring=time.strftime('%M')
print(timemonitaring)
timemonitaring=time.strftime('%S')
print(timemonitaring)
hour=int(time.strftime('%H'))
print(hour)

if hour<12:
    print("Good Morning",s)
elif 12>= hour<=16:
    print("Good Noon",s)
elif 16>= hour <=19:
    print("Good Ahter Noon",s)
else:
    print("Good Night",s)

