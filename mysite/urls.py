"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from company import views
from company import api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('', include('accounts.url')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/list',api.EmpListapi,name='Emplistapi'),
    path('api/list/<int:id>',api.EmpListView.as_view(),name='Emplistapi1'),
    #path('api/list/<int:id>',api.Emp_list2.as_view(),name='Emplist'),
   # path('api/v2/list/<int:id>',api.RetrieveEmpView.as_view(),name='Emplist'),

    path('blockchain',views.blockchain,name='blockchain'),
    path('employee/', views.employee, name="employee"),
    path('department/', views.department, name="department"),



]


