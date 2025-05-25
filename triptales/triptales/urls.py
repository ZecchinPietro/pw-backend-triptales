from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from backend.views import register_view, MyTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('backend/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('backend/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('backend/register/', register_view, name='register'),
]
