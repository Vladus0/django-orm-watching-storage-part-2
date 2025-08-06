def is_visit_long(visit_time, minutes=60):
    time_in_storage = visit_time // minutes
    return time_in_storage > minutes