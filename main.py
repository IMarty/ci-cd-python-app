import datetime

# Get the current hour (24-hour format)
current_hour = datetime.datetime.now().hour
# Other check, code, documentation...

if current_hour < 18:  # Before 6 PM
    print("Hello")
else:  # 6 PM or later
    print("Good night")