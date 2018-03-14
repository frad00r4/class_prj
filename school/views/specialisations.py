# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView

from school.models import Specialisations
from school.serializers import SpecialisationSerializer
from school.permissions import IsAdminOrReadOnly


class RetrieveUpdateDestroySpecialisationsView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = SpecialisationSerializer
    queryset = Specialisations.objects.all()


class ListCreateSpecialisationsView(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminOrReadOnly,)
    serializer_class = SpecialisationSerializer

    def get_queryset(self):
        queryset = Specialisations.objects.all()
        name = self.request.query_params.get('name')
        classes = self.request.query_params.get('classes')
        teachers = self.request.query_params.get('teachers')
        if name:
            queryset = queryset.filter(name__contains=name)
        if classes:
            queryset = queryset.filter(
                classes__in=[i for i in classes.split(',')
                             if i.isdigit()]).distinct()
        if teachers:
            queryset = queryset.filter(
                teachers__in=[i for i in teachers.split(',')
                              if i.isdigit()]).distinct()
        return queryset
