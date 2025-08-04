from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from get_duration import get_duration
from format_duration import format_duration


suspicious_visits = []


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