from django.contrib.auth.models import AbstractUser
from django.db import models
from pulse_api.post.models import Tag

class CustomUser(AbstractUser):
    following_tags = models.ManyToManyField(Tag, through='UserFollowingTag', related_name='followers')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on')
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on')

class UserFollowingTag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user_following_tag'
        # unique_together = ('user', 'tag')