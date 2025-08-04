from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from get_duration import get_duration
from is_visit_long import is_visit_long
from format_duration import format_duration


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
