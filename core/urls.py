from django.contrib import admin
from django.urls import path
from app.views import form_view, results_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', form_view, name='form_view'),
    path('results/', results_view, name='results_view'),
]
