from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class blogs(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    like=models.BooleanField(default=False)
    dislike=models.BooleanField(default=False)
    like_count=models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    likes=models.ManyToManyField(User,related_name='post_likes')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')
    created_at = models.DateTimeField(auto_now_add=True)
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE,default=None)