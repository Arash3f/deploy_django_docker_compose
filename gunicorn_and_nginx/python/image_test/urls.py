from django.urls import include, path
from image_test import views

urlpatterns = [
    path('<int:id>/', views.test_image , name="test_image"),
]