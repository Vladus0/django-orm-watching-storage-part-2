from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        leaved_at = localtime(visit.leaved_at)
        visit_time = leaved_at - entered_at
    else:
        time = localtime()
        visit_time = time - entered_at 
    return visit_time.total_seconds()


def format_duration(duration):
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(((duration % 3600) % 60) // 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


def is_visit_long(visit_time, minutes=60):
    time_in_storage = (visit_time // 60)
    if time_in_storage > minutes:
        return True
    else:
        return False


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for passcard_visit in passcard_visits:
        visit_time = get_duration(passcard_visit)
        duration_visit_time = format_duration(visit_time)
        this_passcard_visits.append( 
            {
                'entered_at': passcard_visit.entered_at,
                'duration': duration_visit_time,
                'is_strange': is_visit_long(visit_time, minutes=60)
                },
            )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
