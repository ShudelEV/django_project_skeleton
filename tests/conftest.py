"""pytest configuration."""
import django
from django.conf import settings


def pytest_configure():
    """Configure pytest."""
    settings.DEBUG = False
    django.setup()
