from django.db import models
from django.conf import settings

class Post(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=255, db_column='title')
    content = models.TextField(db_column='content')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, db_column='user_id')

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title
