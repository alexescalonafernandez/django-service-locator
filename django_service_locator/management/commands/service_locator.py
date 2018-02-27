from django.core.management import BaseCommand
from django.conf import settings
from service_locator import _command


class Command(BaseCommand):
    """

    Custom Django command for generating a _services.py per module folder if any module uses the ServiceProvider
     decorator. The _services.py loads in Service Locator registry the implementations decorated with ServiceProvider
     decorator. For running the command, execute in cmd:
     python manage.py service_locator

     @author: Alexander Escalona Fernández
    """

    def add_arguments(self, parser):
        pass

    def handle(self, **options):
        module_path = settings.BASE_DIR
        _command.generate_providers_configuration(module_path)