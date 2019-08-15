from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myshop import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/realestate/$', views.RS_ViewSet.as_view(), name="RealEstate"),
    url(r'^api/category/$', views.CateViewSet.as_view(), name="Category"),
    url(r'^api-token-auth/', obtain_jwt_token),
]
    
