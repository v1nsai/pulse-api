from django.contrib.auth.models import AbstractUser
from django.db import models
from pulse_api.post.models import Tag

class CustomUser(AbstractUser):
    following_tags = models.ManyToManyField(Tag, through='UserFollowingTag', related_name='followers')

class UserFollowingTag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_following_tag'
        # unique_together = ('user', 'tag')