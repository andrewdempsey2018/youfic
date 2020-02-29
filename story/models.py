from django.db import models

ADVENTURE='Adventure'
FANTASY='Fantasy'
MYSTERY='Mystery'
SCIFI='SciFi'

CATEGORYS = (
        (ADVENTURE, 'Adventure'),
        (FANTASY, 'Fantasy'),
        (MYSTERY, 'Mystery'),
        (SCIFI, 'SciFi'),
    )

class Story(models.Model):
    title = models.CharField(max_length=30, default="")
    author = models.CharField(max_length=30, default="")
    description = models.TextField(max_length=60, default="")
    category = models.CharField(max_length=9, choices=CATEGORYS, default=ADVENTURE)
    text = models.TextField(max_length=3000, default="")
    published = models.DateTimeField(auto_now=True)

    # Method returns the models name as text
    def __str__(self):
        return self.title