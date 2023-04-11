from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views 

urlpatterns = [

    path("base/",views.base,name="base"),
    path("",views.home,name="home"),
    path("chembur/",views.chembur,name="chembur"),
    path("marine/",views.marine,name="marine"),
    path("bandra/",views.bandra,name="bandra"),
    path("ghatkoper/",views.ghatkoper,name="ghatkoper"),
    path("colaba/",views.colaba,name="colaba"),
    path("aboutus/",views.aboutus,name="aboutus"),
    path("map/",views.map,name="map"),
    path("history/",views.history,name="history"),
    path("bandra/#Sea-link/", views.bandra, name="Sea-link"),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)