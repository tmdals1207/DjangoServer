from django.db import models

class Influencer(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  username = models.CharField(max_length=100)
  biography = models.CharField(max_length=300)
  media_count = models.IntegerField()
  follows_count = models.IntegerField()
  followers_count = models.IntegerField()
  
  class Meta:
    managed = False
    db_table = 'influencers'
    

class Post_limmiae(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_limmiae'
    
    
class Post_10_12_16yp(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_10_12_16yp'
    
class Post_b_saem(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_b.saem'
    
class Post_wescsp1121(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_wescsp1121'
    
class Post_vevi_d_live(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_vevi_d_live'
    
class Post_yakstory119(models.Model):
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_yakstory119'