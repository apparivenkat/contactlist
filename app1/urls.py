from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="COntact List API",
      default_version='v1',
      description="Contact API ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@contact.remote"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


from django.urls import path, include

from app1.views import LoginView, RegisterView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
     
]