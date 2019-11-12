from django.db import models


class Employees(models.Model):
    employee_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25, unique=True)
    phone_number = models.CharField(max_length=20, null=True)
    hire_date = models.DateField()
    job_id = models.CharField(max_length=10)
    salary = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    commission_pct = models.DecimalField(max_digits=2, decimal_places=2, null=True)
    manager_id = models.IntegerField(null=True)
    department_id = models.IntegerField(null=True)

    def __str__(self):
        return str(self.employee_id)

    class Meta:
        db_table = 'employees'

