from django.db import models

# Create your models here.
import uuid

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    #UUID、名前、コメント、投稿日
    id          = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name        = models.CharField(verbose_name="名前",max_length=20)
    comment     = models.CharField(verbose_name="コメント",max_length=200)
    post_dt     = models.DateTimeField(verbose_name="投稿日")

    def __str__(self):
        return self.comment


