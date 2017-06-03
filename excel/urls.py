from django.conf.urls import url

from excel import views

urlpatterns = [
    url(r'^export/', views.export_data, name='export_data'),
]