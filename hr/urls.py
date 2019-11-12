from django.conf.urls import url
from django.contrib import admin
from emp import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^emp/list$', views.list_, name='list'),
    url(r'^emp/(\d{1,3})/$', views.details, name='details'),
    url(r'^emp/(\d{1,3})/delete$', views.delete, name='delete'),
    url(r'^emp/update/$', views.update, name='update'),
    url(r'^json/emp_list/$', views.json_emp_list, name='json_emp_list'),
    url(r'^emp/chart/$', views.emp_chart, name='emp_chart'), # highchart로 표현하기 예
    url(r'^emp/chart_view/$', views.emp_chart_view, name='emp_chart_view'),
    #url(r'^emp/sal_pie_chart/$', views.sal_pie_chart, name='sal_pie_chart'),
    url(r'^test$', views.test, name='test')
]
