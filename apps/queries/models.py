from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=256)
    developer = models.ForeignKey(
        "Developer",
        on_delete=models.PROTECT,
        related_name="tasks",
        verbose_name="Assign to",
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["id"]


class Developer(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField(default=18, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
