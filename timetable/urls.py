from django.conf.urls import patterns, include, url
from timetable.views import SubjectListAPIView, SubjectDetailAPIView, TeacherListAPIView, TeacherDetailAPIView,\
    LessonListCreateAPIView, LessonDetailAPIView

urlpatterns = patterns('',
    url(r'^subjects/?$', SubjectListAPIView.as_view(), name="subjects-list-create"),
    url(r'^subjects/(?P<pk>[0-9]+)/?$', SubjectDetailAPIView.as_view(), name="subject-detail"),

    url(r'^teachers/?$', TeacherListAPIView.as_view(), name="teachers-list-create"),
    url(r'^teachers/(?P<pk>[0-9]+)/?$', TeacherDetailAPIView.as_view(), name="teachers-detail"),

    url(r'^lessons/?$', LessonListCreateAPIView.as_view(), name="lessons-list-create"),
    url(r'^lessons/(?P<pk>[0-9]+)/?$', LessonDetailAPIView.as_view(), name="lessons-detail"),
    )
