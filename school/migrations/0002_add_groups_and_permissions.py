# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.management import create_permissions
from django.db import migrations


def add_group_permissions(apps, schema_editor):
    apps.label = 'school'
    apps.models_module = True
    create_permissions(apps, verbosity=0)
    apps.models_module = None
    apps.label = None

    group_model = apps.get_model('auth.Group')
    permission_model = apps.get_model('auth.Permission')

    add_classes_permission = permission_model.objects.get(
        codename='add_classes')
    change_classes_permission = permission_model.objects.get(
        codename='change_classes')
    delete_classes_permission = permission_model.objects.get(
        codename='delete_classes')
    change_teachers_permission = permission_model.objects.get(
        codename='change_teachers')
    delete_teachers_permission = permission_model.objects.get(
        codename='delete_teachers')
    change_students_permission = permission_model.objects.get(
        codename='change_students')
    delete_students_permission = permission_model.objects.get(
        codename='delete_students')

    group, created = group_model.objects.get_or_create(name='teachers')
    if created:
        group.permissions.add(add_classes_permission)
        group.permissions.add(change_classes_permission)
        group.permissions.add(delete_classes_permission)
        group.permissions.add(change_teachers_permission)
        group.permissions.add(delete_teachers_permission)

    group, created = group_model.objects.get_or_create(name='students')
    if created:
        group.permissions.add(change_students_permission)
        group.permissions.add(delete_students_permission)


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
    ]
