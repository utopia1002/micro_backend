from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/realestate/$', views.RS_ViewSet.as_view(), name="RS"),
    url(r'^api/category/$', views.CateViewSet.as_view(), name="Category"),
]
