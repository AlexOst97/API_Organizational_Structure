from django.db import models


class Department(models.Model):

    name = models.CharField(
        max_length=100,
        verbose_name="Название подразделения"
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Название отдела"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания"
    )

    class Meta:
        verbose_name = "Подразделение"
        verbose_name_plural = "Подразделения"

    def __str__(self):
        return f"{self.id} {self.name}"


class Employee(models.Model):

    full_name = models.CharField(
        max_length=255,
        verbose_name="Полное имя сотрудника"
    )

    position = models.CharField(
        max_length=255,
        verbose_name="Должность"
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        verbose_name="Подразделение"
    )

    hired_at = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата найма"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.id} {self.full_name}"