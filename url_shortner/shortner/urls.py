from django.urls import path
from shortner.views.healthcheck import HealthCheckView
from shortner.views.encode import EncodeView

urlpatterns = [
    path('health-check', HealthCheckView.as_view(), name='health-check'),
    path('encode', EncodeView.as_view(), name='encode'),
]