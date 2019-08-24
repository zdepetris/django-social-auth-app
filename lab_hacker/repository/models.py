from django.db import models
from lab_hacker.user.models import User


class Tag(models.Model):
    title = models.CharField(
        'Tag Tittle',
        max_length=35,
        help_text='Ex: Devops, python'
    )

    color = models.CharField(
        'Color',
        max_length=30,
        help_text='Tag Color.'
    )

    def __str__(self):
        return self.name

class Repository(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, related_name='tags')

    def __str__(self):
        return '%d, %s, (%s), (%s)' % (
                self.id,
                self.name,
                self.description,
                ', '.join(tag.name for tag in self.tags.all())
            )
