from django.db import models

# Create your models here.
from django.db.models import permalink
from time import time
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

def generate_imagename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_images/'+str(int(time()))+'.'+ext


class Instructor(models.Model):
    user = models.OneToOneField(User, null=True)
    f_name = models.CharField(max_length=80)
    l_name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    ### how to link a link ????
    twitter = models.URLField(max_length=100, null=True)
    website = models.URLField(max_length=100, null=True)
    git = models.URLField(max_length=100, null=True)
    bio = models.TextField(null=True)
    admin = models.BooleanField(default=False)
    pic = models.ImageField(upload_to=generate_imagename, null=True)


    def __unicode__(self):
        name = self.f_name + ' '+ self.l_name
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

# @receiver(post_delete, sender=Course)
# def stuff_post_delete_handler(sender, **kwargs):
#     Course = kwargs['instance']
#     storage,path = Course.content.storage, Course.content.path
#     storage.delete(path)


def generate_filename(instance, filename):
    ext = filename.split('.')[-1]
    return 'stuff_materials/'+str(int(time()))+'.'+ext

class Material(models.Model):
    TYPE_CHOICE = (('link', 'add a link'), ('file', 'add a file'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=4, choices=TYPE_CHOICE, default='link')
    course = models.ForeignKey(Course)
    date = models.DateTimeField(blank=True, null=True)
    link_content = models.URLField(max_length=500, null=True, blank=True)
    content = models.FileField(upload_to=generate_filename, null=True,blank=True)

    def __unicode__(self):
        return self.name

@receiver(post_delete, sender=Material)
def stuff_post_delete_handler(sender, **kwargs):
    Material = kwargs['instance']
    if Material.content:
        storage,path = Material.content.storage, Material.content.path
        storage.delete(path)


