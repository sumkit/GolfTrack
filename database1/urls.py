from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from golftrack import views

#urls file for the app

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^accounts/profile/', views.profile, name = 'profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/input_round/', views.inputRound, name = 'input_round'),
    url(r'^add-course/', views.addCourse, name = 'add-course'),
    url(r'^courses/', views.CourseList, name = 'courses'),
    url(r'^profile/stats', views.stats, name = 'profile_stats'),
    url(r'^profile/course_stats', views.courseStats, name = 'course_stats'),
    #url(r'^myrounds/$', views.golferRounds.as_view(), name='my-rounds'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^course/(?P<course>[a-zA-Z0-9_.-]+)', views.course,name='course').
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
]
