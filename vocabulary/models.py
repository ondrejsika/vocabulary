from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    user = models.ForeignKey('auth.User')

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s' % self.name


class Topic(models.Model):
    user = models.ForeignKey('auth.User')
    course = models.ForeignKey(Course)

    name = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s %s' % (self.course, self.name)


class Vocabulary(models.Model):
    user = models.ForeignKey('auth.User')
    topic = models.ForeignKey(Topic)

    source = models.CharField(max_length=32)
    target = models.CharField(max_length=32)

    def __unicode__(self):
        return '%s : %s (%s)' % (self.source, self.target, self.topic)

