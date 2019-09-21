from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myshop import views
from rest_framework_jwt.views import obtain_jwt_token
from myshop.models import Real_estate

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/realestate/$', views.RS_ViewSet.as_view(), name="RealEstate"),
    url(r'^api/category/$', views.CateViewSet.as_view(), name="Category"),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api/realestate/landmark/$', views.LandMark.as_view(), name="Landmark"),
    url(r'^api/realestate/commercial/$', views.Commercial.as_view(), name="Commercial"),
    url(r'^api/realestate/residential/$', views.Residential.as_view(), name="Residential"),
    url(r'^api/realestate/(?P<id>\d+)/$', views.Detail.as_view(), name="Detail"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
