# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User, Group
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, \
    PrimaryKeyRelatedField, CharField

from school.models import Classes, Teachers, Specialisations, Students


class SpecialisationSerializer(ModelSerializer):
    classes = PrimaryKeyRelatedField(many=True, read_only=True)
    teachers = PrimaryKeyRelatedField(source='teachers_set',
                                      many=True, read_only=True)

    class Meta(object):
        model = Specialisations
        fields = ('id', 'name', 'classes', 'teachers')


class TeacherSerializer(ModelSerializer):
    classes = PrimaryKeyRelatedField(many=True, read_only=True)
    password = CharField(source='user.password',
                         style={'input_type': 'password'}, write_only=True)
    first_name = CharField(source='user.first_name')
    last_name = CharField(source='user.last_name')
    username = CharField(source='user.username', read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=('%s_%s' % (validated_data['user']['first_name'],
                                 validated_data['user']['last_name'])).lower(),
            password=validated_data['user']['password'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name']
        )

        teachers_group = Group.objects.get(name='teachers')
        user.groups.add(teachers_group)

        teacher = Teachers.objects.create(
            user=user
        )
        teacher.specialisations.add(*validated_data['specialisations'])

        return teacher

    def update(self, instance, validated_data):
        user = User.objects.get(pk=instance.user.id)
        if validated_data['user'].get('password'):
            user.set_password(validated_data['user']['password'])
        user.first_name = validated_data['user'].get('first_name', '')
        user.last_name = validated_data['user'].get('last_name', '')
        user.save()

        instance.specialisations.clear()
        instance.specialisations.add(*validated_data['specialisations'])

        return instance

    class Meta(object):
        model = Teachers
        fields = ('id', 'username', 'first_name', 'last_name',
                  'specialisations', 'password', 'classes')


class ClassSerializer(ModelSerializer):
    students = PrimaryKeyRelatedField(source='students_set',
                                      many=True, read_only=True)
    teacher = PrimaryKeyRelatedField(queryset=Teachers.objects.all())
    specialisation = PrimaryKeyRelatedField(
        queryset=Specialisations.objects.all()
    )

    class Meta(object):
        model = Classes
        fields = ('id', 'name', 'description', 'teacher',
                  'specialisation', 'students')

    def create(self, validated_data):
        if not validated_data['specialisation'] in \
                validated_data['teacher'].specialisations.all():
            raise ValidationError('{} doesn\'t have {} specialisation'.format(
                validated_data['teacher'],
                validated_data['specialisation']
            ))
        return super(ClassSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        if not validated_data['specialisation'] in \
                validated_data['teacher'].specialisations.all():
            raise ValidationError('{} doesn\'t have {} specialisation'.format(
                validated_data['teacher'],
                validated_data['specialisation']
            ))
        return super(ClassSerializer, self).update(instance, validated_data)


class StudentSerializer(ModelSerializer):
    password = CharField(source='user.password',
                         style={'input_type': 'password'}, write_only=True)
    first_name = CharField(source='user.first_name')
    last_name = CharField(source='user.last_name')
    username = CharField(source='user.username', read_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=('%s_%s' % (validated_data['user']['first_name'],
                                 validated_data['user']['last_name'])).lower(),
            password=validated_data['user']['password'],
            first_name=validated_data['user']['first_name'],
            last_name=validated_data['user']['last_name']
        )

        students_group = Group.objects.get(name='students')
        user.groups.add(students_group)

        student = Students.objects.create(
            user=user,
        )

        student.classes.add(*validated_data['classes'])

        return student

    def update(self, instance, validated_data):
        user = User.objects.get(pk=instance.user.id)
        if validated_data['user'].get('password'):
            user.set_password(validated_data['user']['password'])
        user.first_name = validated_data['user'].get('first_name', '')
        user.last_name = validated_data['user'].get('last_name', '')
        user.save()

        instance.classes.clear()
        instance.classes.add(*validated_data['classes'])

        return instance

    class Meta(object):
        model = Students
        fields = ('id', 'username', 'first_name', 'last_name',
                  'password', 'classes')
