"""MiliDeal URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from mainAPI.urls import router as mainAPI_router
from store.urls import router as store_router
from user.urls import router as user_router
from review.urls import router as review_router


root_router = routers.DefaultRouter(trailing_slash=False)
root_router.registry.extend(mainAPI_router.registry)
root_router.registry.extend(store_router.registry)
root_router.registry.extend(user_router.registry)
root_router.registry.extend(review_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(root_router.urls)),
    path('user/', include('user.urls')),
]