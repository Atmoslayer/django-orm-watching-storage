import datetime
import pytz

from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        uts3_time_entered_at = self.entered_at.astimezone(pytz.timezone('Europe/Moscow'))
        if self.leaved_at:
            uts3_time_leaved_at = self.leaved_at.astimezone(pytz.timezone('Europe/Moscow'))
            visit_duration = uts3_time_leaved_at - uts3_time_entered_at
        else:
            time_now = datetime.datetime.now()
            uts3_time_now = time_now.astimezone(pytz.timezone('Europe/Moscow'))
            visit_duration = uts3_time_now - uts3_time_entered_at
        return uts3_time_entered_at, visit_duration


def format_duration(duration):
    duration_seconds = duration.seconds
    duration_hours = duration_seconds // 3600
    duration_minutes = (duration_seconds % 3600) // 60
    str_time = f'{duration_hours} ч, {duration_minutes} мин'
    return str_time


def is_visit_long(duration):
    duration_seconds = duration.seconds
    duration_hours = duration_seconds // 3600
    if duration_hours < 1:
        return False
    else:
        return True
