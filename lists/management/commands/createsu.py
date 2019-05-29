from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="lester").exists():
            User.objects.create_superuser("lester", "lester_wu@raytrex.com", "mniwxy0918")