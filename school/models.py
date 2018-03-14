# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Specialisations(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False,
                            max_length=255, unique=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Teachers(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        related_name='teacher_profile',
        on_delete=models.CASCADE,
        null=False
    )
    specialisations = models.ManyToManyField(Specialisations)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)


@python_2_unicode_compatible
class Classes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    teacher = models.ForeignKey(Teachers, related_name='classes',
                                on_delete=models.CASCADE)
    specialisation = models.ForeignKey(Specialisations,
                                       related_name='classes',
                                       on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.name, self.description)


@python_2_unicode_compatible
class Students(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User,
        related_name='student_profile',
        on_delete=models.CASCADE,
        null=False
    )
    classes = models.ManyToManyField(Classes)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)
