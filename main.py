import datetime

# Get the current hour (24-hour format)
current_hour = datetime.datetime.now().hour
# Other check, code, documentation...
if current_hour < 13:  # Before 6 PM
    print("Hello")
elif current_hour >18:  # 6 PM or later
    print("Good night")
elif current_hour >=13 :
    print("Good afternoon")    
else: 
    print("Time?")    