from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard_object = Passcard.objects.filter(is_active=True, passcode=passcode)
    passcard = passcard_object[0]
    this_passcard_visits_serialized = []
    passcard_visits = Visit.objects.filter(passcard=passcard)

    for visit in passcard_visits:
        entered_at, visit_duration = visit.get_duration()
        is_strange = is_visit_long(visit_duration)

        this_passcard_visits_serialized.append(
            {
                'entered_at': entered_at,
                'duration': visit_duration,
                'is_strange': is_strange
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_serialized
        }
    return render(request, 'passcard_info.html', context)
