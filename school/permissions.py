# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.permissions import BasePermission, \
    DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or \
               request.user and request.user.is_staff


class DjangoModelPermissionsAndOwnerOrAnonReadOnly(DjangoModelPermissionsOrAnonReadOnly):  # noqa: E501
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or \
               request.user and request.user.is_staff:
            return True

        return obj.user == request.user
