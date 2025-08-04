def format_duration(duration):
    seconds_in_hour = 3600
    minutes_in_hour = 60
    seconds_in_minute = 60
    hours = int(duration // seconds_in_hour)
    minutes = int((duration % seconds_in_hour) // minutes_in_hour)
    seconds = int(((duration % seconds_in_hour) % minutes_in_hour) // seconds_in_minute)
    return f"{hours:02}:{minutes:02}:{seconds:02}"