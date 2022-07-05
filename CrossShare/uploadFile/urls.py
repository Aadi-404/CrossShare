from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import  re_path
from uploadFile.views import fileListCreateView,fileRetreiveUpdateDestroyView
urlpatterns = [
    path('file/',fileListCreateView.as_view()),
    path('file/<int:pk>',fileRetreiveUpdateDestroyView.as_view()),
    re_path(r'^file/(?P<uuid>.+)/$', fileListCreateView.as_view()),
    # re_path(r'^download/(?P<unique>.+)/$', fileRetreiveUpdateDestroyView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
