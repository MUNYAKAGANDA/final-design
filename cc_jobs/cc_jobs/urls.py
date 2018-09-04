"""cc_jobs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from courses.views	import	CourseListView
from app.views import ActivityViews



urlpatterns = [
     path('',ActivityViews.as_view(),name='activity_view'),
    # path('',views.ArticleViews.as_view(),name='articleview'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    path('course/', include('courses.urls',namespace='courses')),
    # path('list',	CourseListView.as_view(),	name='course_list'),

    path('students/', include('students.urls')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('app/',include('app.urls',namespace='app')),
    path('list', CourseListView.as_view(), name='course_list'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)