from datetime import datetime

def get_current_datetime():
    time = datetime.now().strftime('%d.%m.%Y')
    return time