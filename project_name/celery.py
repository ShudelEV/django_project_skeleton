"""Celery app."""
import os
from typing import Optional

from celery import Celery, Task
from kombu import Exchange, Queue

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")

app: Celery = Celery("project_name")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.worker_hijack_root_logger = False
app.conf.task_ignore_result = True
app.conf.task_store_errors_even_if_ignored = True

app.conf.task_queues = (
    Queue("normal", Exchange("normal"), routing_key="normal"),
    Queue("low", Exchange("low"), routing_key="low"),
)
app.conf.task_default_queue = "normal"
app.conf.task_default_exchange = "normal"
app.conf.task_default_routing_key = "normal"

app.conf.task_routes = {
    # example:
    # "users.tasks.send_firebase_notification": {"queue": "normal"},
}


def retry_task(
        task: Task,
        exception: Optional[Exception] = None,
        max_attempts: Optional[int] = None,
) -> None:
    """
    Retry celery tasks.

    Retries the specified task using a "backing off countdown",
    meaning that the interval between retries grows exponentially
    with every retry.

    :param task: The task to retry.
    :param exception: Optionally, the exception that caused the retry.
    :param max_attempts: Optionally, number of maximum attempts to retry the task.
    """

    def backoff(attempts: int) -> int:
        return 5 * (2 ** attempts)

    kwargs: dict = {
        "countdown": backoff(task.request.retries),
    }

    if exception:
        kwargs["exc"] = exception

    if not max_attempts or task.request.retries < max_attempts:
        raise task.retry(**kwargs)
