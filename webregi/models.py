from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    publisher = models.CharField(max_length=200)
    publisher_logo = models.ImageField(upload_to='publisher_logo/%Y/%m/%d/')
    image = models.ImageField(upload_to='article_image/%Y/%m/%d/')
    slug = models.SlugField(max_length=200, unique=True)
    name_author = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

class Photography(models.Model):
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photography_image/%Y/%m/%d/')
    place = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='photo_posts')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

class Award(models.Model):
    award_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    link_award = models.URLField(max_length=500)

    def __str__(self):
        return self.award_name

class Certification(models.Model):
    certification_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    link_certification = models.URLField(max_length=500)

    def __str__(self):
        return self.certification_name

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    framework = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    link_project = models.URLField(max_length=500)

    def __str__(self):
        return self.project_name

class Publication(models.Model):
    publication_name = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    link_publication = models.URLField(max_length=500)

    def __str__(self):
        return self.publication_name

class Programing(models.Model):
    programing_name = models.CharField(max_length=200)
    level = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(1.0)],
    )
    logos = models.ImageField(upload_to='programing_logos/%Y/%m/%d/')

    def __str__(self):
        return self.programing_name
