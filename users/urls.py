from django.urls import path, include


urlspatterns = [
    path('api-auth/', include('rest_framework.urls'))
]