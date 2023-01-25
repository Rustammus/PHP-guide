from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path("", views.index, name="home"),
    path("demand", views.demand, name="demand"),
    path("geography", views.geography, name="geography"),
    path("skills", views.skills, name="skills"),
    path("recentvacancies", views.recentvacancies, name="recvac")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
