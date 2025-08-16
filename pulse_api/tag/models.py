# In pulse_api/post/models.py (or another appropriate app)
from django.db import models

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='name', max_length=255)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name