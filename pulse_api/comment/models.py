from django.db import models
from django.conf import settings

class Comment(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    post_id = models.ForeignKey('posts.Post', on_delete=models.CASCADE, db_column='post_id')
    content = models.TextField(db_column='content')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, db_column='user_id')

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content
