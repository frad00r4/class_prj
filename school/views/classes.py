from __future__ import unicode_literals

from rest_framework.authentication import SessionAuthentication, \
    BasicAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, \
    ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from school.models import Classes
from school.serializers import ClassSerializer


class RetrieveUpdateDestroyClassesView(RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Classes.objects.all()
    serializer_class = ClassSerializer


class ListCreateClassesView(ListCreateAPIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)
    serializer_class = ClassSerializer

    def get_queryset(self):
        queryset = Classes.objects.all()
        name = self.request.query_params.get('name')
        description = self.request.query_params.get('description')
        teachers = self.request.query_params.get('teachers')
        specialisations = self.request.query_params.get('specialisations')
        students = self.request.query_params.get('students')
        if name:
            queryset = queryset.filter(name__contains=name)
        if description:
            queryset = queryset.filter(description__contains=description)
        if teachers:
            queryset = queryset.filter(
                teacher__in=[i for i in teachers.split(',') if i.isdigit()])
        if specialisations:
            queryset = queryset.filter(specialisation=specialisations)
        if students:
            queryset = queryset.filter(
                students__in=[i for i in students.split(',')
                              if i.isdigit()]).distinct()
        return queryset
