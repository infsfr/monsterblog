from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

    @models.permalink
    def get_absolute_url(self):
        return ('tag', [self.slug])

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']
