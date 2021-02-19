from django.urls import include, path, re_path
from repks.apps.hello_repka.api.v1.views.views import HelloRepkaView

urlpatterns = [
    path('', HelloRepkaView.as_view())
]
