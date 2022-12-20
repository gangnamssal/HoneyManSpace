from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 좋아요 기능
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_movie')
    # 영화 제목
    title = models.CharField(max_length = 20)
    # 관객 수
    audience = models.IntegerField()
    # 개봉일
    release_date = models.DateField()
    # 장르
    genre = models.CharField(max_length = 30)
    # 평점
    score = models.FloatField()
    # 포스터 경로
    poster_url = models.TextField()
    # 줄거리
    description = models.TextField()

class Comment(models.Model):
    movie = models.ForeignKey(Movie,on_delete = models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
