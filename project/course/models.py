from django.db import models

# Create your models here.
from django.db.models import permalink
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

def generate_imagename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_images/'+str(int(time()))+'.'+ext


class Instructor(models.Model):
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
    pic = models.ImageField(upload_to=generate_imagename)


    def __unicode__(self):
        name = self.f_name + self.l_name
        return name


    @permalink
    def get_absolute_url(self):
        return('instructors', (), {
            'slug': self.name,
            'pk':self.pk,
        })

@receiver(post_delete, sender=Instructor)
def stuff_post_delete_handler(sender, **kwargs):
    Instructor = kwargs['instance']
    storage,path = Instructor.pic.storage, Instructor.pic.path
    storage.delete(path)


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

def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_materials/'+str(int(time()))+'.'+ext

class Material(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    course = models.ForeignKey(Course)
    date = models.DateTimeField(blank=True, null=True)
    content = models.FileField(upload_to=generate_filename, default=False)

    def __unicode__(self):
        return self.name

@receiver(post_delete, sender=Instructor)
def stuff_post_delete_handler(sender, **kwargs):
    Instructor = kwargs['instance']
    storage,path = Instructor.content.storage, Instructor.content.path
    storage.delete(path)
