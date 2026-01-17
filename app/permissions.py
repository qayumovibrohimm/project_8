import datetime
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsKayumBlocked(BasePermission):
    def has_permission(self, request, view):
        if request.user.username == 'kayum':
            return False
        return True


class WorkDay(BasePermission):
    def has_permission(self, request, view):
        today = datetime.date.today().weekday()
        worked_at = datetime.datetime.now().hour
        return (7 <= worked_at) < 21 and (0 <= today <= 6)


from rest_framework.permissions import BasePermission
from django.utils import timezone
from datetime import timedelta


class CanUpdateWithin4Hours(BasePermission):
    message = "You can edit this object within 4 hours"

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        if request.method in ['PUT', 'PATCH']:
            now = timezone.now()
            allowed_time = obj.created_at + timedelta(hours=4)

            return now <= allowed_time


        return True

