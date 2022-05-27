from datacenter.models import format_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    non_closed_visits_serialized = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for non_closed_visit in non_closed_visits_serialized:
        entered_time, visit_duration = non_closed_visit.get_duration()
        formated_duration = format_duration(visit_duration)
        who_entered = non_closed_visit.passcard

        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_time,
                'duration': formated_duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
