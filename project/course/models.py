from django.db import models

# Create your models here.
from django.db.models import permalink


class Instructor(models.Model):
    user = models.OneToOneField(User, null=True)
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    ### how to link a link ????
    twitter = models.URLField(max_length=100)
    website = models.URLField(max_length=100)
    git = models.URLField(max_length=100)
    bio = models.TextField()
    admin = models.BooleanField(default=False)
    pic = models.ImageField(upload_to='blah', default='path/to/my/default/image.jpg')


    def __unicode__(self):
        name = self.f_name + self.l_name
        return name


    @permalink
    def get_absolute_url(self):
        return('instructors', (), {
            'slug': self.name,
            'pk':self.pk,
        })

class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Course(models.Model):
    c_name = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor')
    level = models.CharField(max_length=20)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    meetup_page = models.URLField(max_length=200)
    topic = models.ForeignKey('Topic')
    description = models.TextField()
    prerequisite = models.TextField()

    @permalink
    def get_absolute_url(self):
        return('courses', (), {
            'slug': self.c_name,
            'pk':self.pk,
        })

    def __unicode__(self):
        return self.c_name

class Material(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    course_id = models.ForeignKey(Course)
    date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.name

