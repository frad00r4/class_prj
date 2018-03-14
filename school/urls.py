# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from school.views.classes import RetrieveUpdateDestroyClassesView, \
    ListCreateClassesView
from school.views.teachers import RetrieveUpdateDestroyTeachersView, \
    ListCreateTeachersView
from school.views.students import RetrieveUpdateDestroyStudentView, \
    ListCreateStudentsView
from school.views.specialisations import \
    RetrieveUpdateDestroySpecialisationsView, ListCreateSpecialisationsView


urlpatterns = [
    url(r'^classes/(?P<pk>\d+)/$',
        RetrieveUpdateDestroyClassesView.as_view(), name='classes'),
    url(r'^classes/$', ListCreateClassesView.as_view(), name='classes-list'),

    url(r'^teachers/(?P<pk>\d+)$',
        RetrieveUpdateDestroyTeachersView.as_view(), name='teachers'),
    url(r'^teachers/$', ListCreateTeachersView.as_view(),
        name='teachers-list'),

    url(r'^students/(?P<pk>\d+)$',
        RetrieveUpdateDestroyStudentView.as_view(), name='students'),
    url(r'^students/$',
        ListCreateStudentsView.as_view(), name='students-list'),

    url(r'^specialisations/(?P<pk>\d+)$',
        RetrieveUpdateDestroySpecialisationsView.as_view(),
        name='specialisations'),
    url(r'^specialisations/$',
        ListCreateSpecialisationsView.as_view(), name='specialisations-list')
]
