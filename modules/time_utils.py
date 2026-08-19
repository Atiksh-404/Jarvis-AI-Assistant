from datetime import datetime

def get_time():
    current_time = datetime.now().strftime("%I:%M %p")
    return f"The current time is {current_time}"