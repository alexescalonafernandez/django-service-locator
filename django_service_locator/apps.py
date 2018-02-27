from django.apps import AppConfig
from django.conf import settings
from service_locator import _command


class ServiceLocatorConfig(AppConfig):
    name = 'django_service_locator'

    def ready(self):
        """
        This function is executed when django app is ready. The goal of this function is to scan the modules folder for
        importing all the _services.py scripts for populating the Service Locator registry.
        :return: 

        @author: Alexander Escalona Fernández
        """
        module_path = settings.BASE_DIR
        _command.populate_service_locator_registry(module_path)