from typing import Union
from django.db import models

# from django.contrib.auth.models import User
from django.db.models import Q

from .models import Developer, Task
from .constant import LOOKUP_SEP, SENIOR_AGE

# from apps.queries.shell import *
# from apps.queries.models import Task, Developer


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


def find_devs_by_start_or_end_char(char: str) -> models.QuerySet:
    return Developer.objects.filter(Q(name__istartswith=char) | Q(name__iendswith=char))


def create_lookups(*args):
    lookups = [
        Q(name__istartswith=char) | Q(name__istartswith=args[args.index(char) + 1])
        for char in args
        if char != args[-1]
    ]
    return lookups


def qs_filter(
    qs: models.QuerySet, field: str, expression: str, value
) -> models.QuerySet:
    lookup = LOOKUP_SEP.join([field, expression])
    return qs.filter(**{lookup: value})


def find_devs_by_start_chars(*args) -> models.QuerySet:
    return Developer.objects.filter(*create_lookups(*args))


# TODO: find the best solution for dynamic filter
def find_devs_by_start_chars2(*args):
    pass


# from apps.queries.shell import *
