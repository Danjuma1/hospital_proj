from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blogpost(models.Model):
    CATEGORIES = (
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization')
    )

    STATUS = (
    (0,"Draft"),
    (1,"Publish")
    )

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='images/BlogImages')
    content = models.TextField(max_length=40000)
    summary = models.CharField(max_length=1500)
    status = models.IntegerField(choices=STATUS, default=1)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    created_date = models.DateTimeField(default = timezone.now)
    class Meta:
        ordering = ['-created_date']

    def __str__(self):
	    return self.title