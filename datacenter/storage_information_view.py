from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


suspicious_visits = []

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


def storage_information_view(request):
    not_closed_visits = Visit.objects.filter(leaved_at=None)

    visits = []


    for not_closed_visit in not_closed_visits:
        visit_time = get_duration(not_closed_visit)


        visits.append(
            {
                'who_entered': not_closed_visit.passcard,
                'entered_at': not_closed_visit.entered_at,
                'duration': format_duration(visit_time),
            }
        )

    context = {
        'non_closed_visits': visits, 
    }
    
    return render(request, 'storage_information.html', context)