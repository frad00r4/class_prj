# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import AllowAny

from school.models import Students
from school.serializers import StudentSerializer
from school.permissions import DjangoModelPermissionsAndOwnerOrAnonReadOnly


class RetrieveUpdateDestroyStudentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissionsAndOwnerOrAnonReadOnly,)
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class ListCreateStudentsView(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (AllowAny,)
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Students.objects.all()
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        classes = self.request.query_params.get('classes')
        username = self.request.query_params.get('username')
        if username is not None:
            queryset = queryset.filter(user__username__contains=username)
        if first_name is not None:
            queryset = queryset.filter(
                user__first_name__contains=first_name)
        if last_name is not None:
            queryset = queryset.filter(user__last_name__contains=last_name)
        if classes is not None:
            queryset = queryset.filter(
                classes__in=[i for i in classes.split(',')
                             if i.isdigit()]).distinct()
        return queryset
