from django.db import models
from django.conf import settings

class Post(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=255, db_column='title')
    content = models.TextField(db_column='content')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, db_column='user_id')
    tags = models.ManyToManyField('tag.Tag', through='PostHasTag', related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True, db_column='created_on')
    updated_on = models.DateTimeField(auto_now=True, db_column='updated_on')

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

class PostHasTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE)

    class Meta:
        db_table = 'post_has_tag'

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post_images/')

    class Meta:
        db_table = 'post_image'

    def save(self, *args, **kwargs):
        # up to 10 images per post
        if self.post.images.count() >= 10:
            raise ValueError("A post cannot have more than 10 images.")
        super().save(using='s3', *args, **kwargs)