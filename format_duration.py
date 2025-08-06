def format_duration(duration):
    total_seconds = duration
    seconds_in_hour = 3600
    minutes_in_hour = 60
    seconds_in_minute = 60
    hours = int(total_seconds // seconds_in_hour)
    minutes = int((total_seconds % seconds_in_hour) // minutes_in_hour)
    seconds = int(total_seconds % seconds_in_minute)
    return f"{hours:02}:{minutes:02}:{seconds:02}"