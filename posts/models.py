from django.db import models
from categories.models import Category
from tags.models import Tag


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    perex = models.TextField()
    content = models.TextField()
    views_count = models.IntegerField(default=0)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('post', [self.slug])

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
