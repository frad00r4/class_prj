# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView

from school.models import Teachers
from school.serializers import TeacherSerializer
from school.permissions import IsAdminOrReadOnly, \
    DjangoModelPermissionsAndOwnerOrAnonReadOnly


class RetrieveUpdateDestroyTeachersView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissionsAndOwnerOrAnonReadOnly,)
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer


class ListCreateTeachersView(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = TeacherSerializer

    def get_queryset(self):
        queryset = Teachers.objects.all()
        username = self.request.query_params.get('username')
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        specialisations = self.request.query_params.get('specialisations')
        classes = self.request.query_params.get('classes')
        if username:
            queryset = queryset.filter(user__username__contains=username)
        if first_name:
            queryset = queryset.filter(user__first_name__contains=first_name)
        if last_name:
            queryset = queryset.filter(user__last_name__contains=last_name)
        if specialisations:
            queryset = queryset.filter(
                specialisations__in=[i for i in specialisations.split(',')
                                     if i.isdigit()]).distinct()
        if classes:
            queryset = queryset.filter(
                classes__in=[i for i in classes.split(',')
                             if i.isdigit()]).distinct()
        return queryset
