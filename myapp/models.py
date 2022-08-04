from statistics import mode
from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Section(models.Model):
    sect=models.CharField(blank=True,max_length=100,default='cse')

    def __str__(self):
        return self.sect

class Student(models.Model):
    name=models.CharField(max_length=200,default=0)
    father=models.CharField(max_length=200,default='my_father')
    slug=models.SlugField(blank=True)
    s=models.ForeignKey(Section,null=True,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def save(self):
        self.slug=slugify(self.name)
        super(Student,self).save()

    def get_absolute_url(self):
        return reverse('student',args=[str(self.slug)])
