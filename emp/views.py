import json

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Avg, F, IntegerField
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect

from emp.models import Employees
from django.views.generic.base import TemplateView
from emp.forms import EmpForm


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        return context


def list_(request):
    emp_list = Employees.objects.all().order_by('-employee_id')
    context = {'emp_list': emp_list}
    return render(request, 'emp/list.html', context)


def details(request, employee_id):
    emp = get_object_or_404(Employees, pk=employee_id)
    # context = {'emp': emp}
    context = {'emp': EmpForm(instance=emp)}
    return render(request, "emp/details.html", context)


def delete(request, employee_id):
    get_object_or_404(Employees, pk=employee_id).delete()
    return redirect("/emp/list")


def update(request):
    if request.method == 'GET':
        emp_form = EmpForm()
    else:
        try:
            emp = Employees.objects.get(employee_id=request.POST['employee_id'])
            # from emp.forms import EmpForm
        except ObjectDoesNotExist:
            # from django.core.exceptions import ObjectDoesNotExist
            emp_form = EmpForm(request.POST)
        else:
            emp_form = EmpForm(request.POST, instance=emp)

        if emp_form.is_valid():
            print("form is valid")
            emp_form.save()
            return redirect("/emp/list")
        else:
            print("form is not valid")

    return render(request, 'emp/details.html', {'emp': emp_form})


def test(request):
    return render(request, "test.html")


def json_emp_list(request):
    # emp_list = Employees.objects.all().values("employee_id", "salary")
    # filter(변수명__연산자=값)
    # https://docs.djangoproject.com/en/dev/ref/models/querysets/
    # 급여가 5000보다 큰 사원들의 사원아이디와 급여를 출력하세요
    # emp_list = Employees.objects.filter(salary__gt=5000).values("employee_id", "salary")
    # select employee_is, salary from employees where salary > 5000
    emp_list = Employees.objects.values("department_id")\
        .annotate(avg=Avg('salary')).order_by("department_id")
    return JsonResponse(list(emp_list), safe=False)


def emp_chart(request):
    # data = [{"name": "Chrome", "y": 130, "sliced": "false", "selected": "true"},
    #         {"name": "IE", "y": 100},
    #         {"name": "Firefox", "y": 70}]
    data = Employees.objects.values("department_id") \
        .annotate(name=F("department_id"), y=Cast(Avg('salary'), IntegerField()))\
        .order_by("department_id")
    return JsonResponse(list(data), safe=False)


def emp_chart_view(request):
    return render(request, "emp/emp_chart.html")
