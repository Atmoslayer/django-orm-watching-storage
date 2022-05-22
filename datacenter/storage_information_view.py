from datacenter.models import format_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    in_vault = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for visit in in_vault:
        entered_time, visit_duration = Visit.get_duration(visit)
        formated_duration = format_duration(visit_duration)
        who_entered = visit.passcard

        non_closed_visits.append(
            {
                'who_entered': who_entered,
                'entered_at': entered_time,
                'duration': formated_duration,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
