from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.department, name='department'),
    path('chapters/<int:course_id>', views.chapters, name='chapters'),
    path('course/<int:department_id>', views.course, name='course'),
    path('list_depatment/', views.listDepartments,name='list_department'),
    path('list_chapter/', views.listChapter,name='list_chapter'),
    path('list_courses/', views.listCourses,name='list_courses'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)