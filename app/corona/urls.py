from django.urls import path
from corona.presentation_layer.views.index_view import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
