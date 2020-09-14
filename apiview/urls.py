from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.showIndex.as_view(),name="main"),
    path('product_operations/',views.productOperations.as_view(),name='product_operations'),
]
