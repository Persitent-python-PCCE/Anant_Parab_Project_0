import datetime
import os

def log_event(event, user_id=None):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_message = f"[{timestamp}] Action: {event}"
    if user_id:
        log_message += f" | User ID: {user_id}"
    
    print(log_message)
    current_dir = os.path.dirname(__file__)
    log_file_path = os.path.join(current_dir, "app.log")
    with open(log_file_path, "a") as file:
        file.write(log_message + "\n")
