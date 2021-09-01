from typing import Union
from django.db import models
from .models import Developer, Task

# from apps.queries.shell import *
# from apps.queries.models import Task, Developer

SENIOR_AGE = 30


def developers_list() -> models.QuerySet:
    return Developer.objects.all()


def tasks_list() -> models.QuerySet:
    return Task.objects.all()


def find_tasks_for(developer: Developer) -> models.QuerySet:
    return developer.tasks.all()


def get_sql_string(qs: models.QuerySet) -> str:
    return str(qs.query)


def find_by_age_range(start: int, end: int) -> models.QuerySet:
    return Developer.objects.filter(age__range=[start, end])


def find_seniors_dev() -> models.QuerySet:
    return Developer.objects.filter(age__gte=SENIOR_AGE)


def find_by_age(age: Union[int, str]) -> models.QuerySet:
    return Developer.objects.filter(age=age)
