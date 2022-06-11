from django.urls import path

from uploadFile.views import fileListCreateView,fileRetreiveUpdateDestroyView
urlpatterns = [
    path('file/',fileListCreateView.as_view(),name = 'data_Bundle'),
    path('<int:pk>',fileRetreiveUpdateDestroyView.as_view()),
]
