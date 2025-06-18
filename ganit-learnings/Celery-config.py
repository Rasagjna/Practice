import os
from logging.config import dictConfig

from celery import Celery
from celery.signals import setup_logging
from django.conf import settings

from config import APP_CONFIG
from config.logging import get_logging_config_dict
# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "service.django_settings")


app = Celery("service")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")
# Load config from dictionary (Yaml file)
app.conf.update(**APP_CONFIG.CELERY_SETTINGS.CELERY_ENGINE)

 # Add loggers for each module (So that these modules can simply initiate loggers using logging.getLogger(__name__))
additional_loggers = [
    "utils",
    "tests",
    "ai_insights_management",
    "prescription_metadata_extraction",
]

@setup_logging.connect
def config_loggers(*args, **kwargs):
    """Use celery.task logger for all celery logging."""
    print("Configuring Celery logging...")
    dictConfig(
        get_logging_config_dict(
            service_name=APP_CONFIG.SERVICE_NAME,
            log_level=APP_CONFIG.SERVICE_SETTINGS.LOG_LEVEL,
            additional_loggers=additional_loggers,
        )
    )
# Load task modules from all registered Django apps.
# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
app.autodiscover_tasks(lambda: settings.CODE_APPS)
# CODE_APPS


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


if __name__ == "__main__":
    app.start()
