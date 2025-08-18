from django.db import models
from django.conf import settings

class Comment(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    post_id = models.ForeignKey('post.Post', on_delete=models.CASCADE, db_column='post_id')
    content = models.TextField(db_column='content')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, db_column='user_id')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on')
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on')

    class Meta:
        db_table = 'comment'

    def __str__(self):
        return self.content
