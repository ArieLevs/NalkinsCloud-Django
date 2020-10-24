from django.urls import path

from nalkinscloud_api import views_api, views_devices_api

app_name = 'nalkinscloud_api'

urlpatterns = [
    # REST API urls
    path('readiness/', views_api.ReadinessProbe.as_view(), name='readiness'),
    path('liveness/', views_api.LivenessProbe.as_view(), name='liveness'),
    path('register/', views_api.RegistrationView.as_view(), name='register'),
    path('health_check/', views_api.HealthCheckView.as_view(), name='health_check'),  # Auth require
    path('forgot_password/', views_api.ForgotPasswordView.as_view(), name='forgot_password'),
    path('get_scheduled_job/', views_api.GetScheduledJobView.as_view(), name='get_scheduled_job'),  # Auth require
    path('reset_password/', views_api.ResetPasswordView.as_view(), name='reset_password'),  # Auth require
    path('set_scheduled_job/', views_api.SetScheduledJobView.as_view(), name='set_scheduled_job'),  # Auth require
    path('del_scheduled_job/', views_api.DelScheduledJobView.as_view(), name='del_scheduled_job'),  # Auth require
    path('update_device_pass/', views_api.UpdateMQTTUserPassView.as_view(), name='update_device_pass'),  # Auth require

    # Devices api
    path('customer_device/<str:c_device_id>/', views_devices_api.CustomerDevicesView.as_view(), name='customer_device'),
    path('device_activation/', views_devices_api.DeviceActivationView.as_view(), name='device_activation'),
    path('device_list/', views_devices_api.DeviceListView.as_view(), name='device_list'),
    path('get_device_pass/', views_devices_api.GetDevicePassView.as_view(), name='get_device_pass'),
    path('remove_device/', views_devices_api.RemoveCustomerDeviceView.as_view(), name='remove_device'),
]
