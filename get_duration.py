from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_at = localtime(visit.leaved_at)
        visit_time = leaved_at - entered_at
    else:
        time = localtime()
        visit_time = time - entered_at 
    return visit_time.total_seconds()