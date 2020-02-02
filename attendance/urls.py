from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path(r'home/', views.home, name='home'),
    path(r'course_detail/<str:id>', views.course_detail, name='course_detail'),
    path(r"check-in/<str:id>", views.check_in, name="check_in")
]
