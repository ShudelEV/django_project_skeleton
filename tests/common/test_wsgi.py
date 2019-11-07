from django.core.handlers.wsgi import WSGIHandler

from project_name import wsgi


def test_handler():
    assert type(wsgi.application) is WSGIHandler
