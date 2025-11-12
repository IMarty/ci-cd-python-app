import datetime

def get_greeting():
    # Get the current hour (24-hour format)
    current_hour = datetime.datetime.now().hour
    # Other check, code, documentation...
    if current_hour < 13:  # Before 6 PM
        return "Hello"
    elif current_hour >18:  # 6 PM or later
        return "Good night"
    elif current_hour >=13 :
        return "Good afternoon"    
    else: 
        return "Time?"    
if __name__ == "__main__":
    print(get_greeting())