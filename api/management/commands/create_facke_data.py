from django.core.management.base import BaseCommand
from core.fake_data import Create

class Command(BaseCommand):
    help = 'Create facke data'
    def handle(self, *args, **kwargs):
       Create.create()






