from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcards = Passcard.objects.filter(is_active=True, passcode=passcode)
    this_passcard_visits = []

    for passcard in passcards:
        passcard_visits = Visit.objects.filter(passcard=passcard)

        for visit in passcard_visits:
            entered_at, visit_duration = Visit.get_duration(visit)
            is_strange = is_visit_long(visit_duration)

            this_passcard_visits.append(
                {
                    'entered_at': entered_at,
                    'duration': visit_duration,
                    'is_strange': is_strange
                },
            )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
