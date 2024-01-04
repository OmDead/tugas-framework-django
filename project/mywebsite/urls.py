from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^sosmed/', include('sosmed.urls',namespace='sosmed')),
    url(r'^blog/', include('blog.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
]
