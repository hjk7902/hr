from django import forms
from emp.models import Employees


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone_number',
                  'hire_date', 'job_id', 'salary', 'commission_pct', 'manager_id', 'department_id']
        # fields 속성 또는 exclude 속성 중 하나는 반드시 있어야 함

