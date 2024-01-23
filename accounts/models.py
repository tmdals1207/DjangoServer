from django.db import models

# Create your models here.

class Influencer(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  username = models.CharField(max_length=100)
  biography = models.CharField(max_length=300)
  media_count = models.IntegerField()
  follows_count = models.IntegerField()
  followers_count = models.IntegerField()
  category = models.CharField(max_length=100)
  adv_count = models.IntegerField()
  week_avg_post = models.DecimalField(max_digits=5, decimal_places=1)
  am_pm = models.CharField(max_length=100)
  avg_post_time = models.CharField(max_length=100)
  feed_percent = models.IntegerField()
  reels_percent = models.IntegerField()
  avg_comments = models.IntegerField()
  avg_goods = models.IntegerField()
  comments_percent = models.IntegerField()
  goods_percent = models.IntegerField()
  profile_url = models.TextField()
  company = models.CharField(max_length=100)
  recent_adv = models.CharField(max_length=100)
  
  class Meta:
    managed = False
    db_table = 'influencers'
    
    
class Post_master(models.Model):
  username = models.CharField(max_length=100)
  post_id = models.CharField(max_length=100, primary_key=True)
  caption = models.TextField(max_length=10000)
  comments_count = models.IntegerField()
  like_count = models.IntegerField()
  media_type = models.CharField(max_length=100)
  timestamp = models.CharField(max_length=100)
  owner_id = models.CharField(max_length=100)
   
  class Meta:
    managed = False
    db_table = 'post_master'
    
    
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
    
class Post_iam_yaksa(models.Model):
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
    db_table = 'post_iam_yaksa'
    
class Post_yakstagram(models.Model):
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
    db_table = 'post_yakstagram'
    
class Post_pt_jjuny(models.Model):
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
    db_table = 'post_pt__jjuny'
    
class User_adv(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  company = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  business = models.CharField(max_length=100)
  size = models.CharField(max_length=100)
  client = models.IntegerField()
  campaign_progress = models.IntegerField()
  
  class Meta:
    managed = False
    db_table = 'user_adv'
    
class User_influ(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  instagram_id = models.CharField(max_length=100)
  password = models.CharField(max_length=100)
  business = models.CharField(max_length=100)
  followers_count = models.CharField(max_length=100)
  
  class Meta:
    managed = False
    db_table = 'user_influ'
    
class Keyword(models.Model):
  id=models.CharField(max_length=100)
  username = models.CharField(max_length=100)
  words = models.CharField(max_length=100)
  weights = models.DecimalField(max_digits=15, decimal_places=10, primary_key=True)  # 소수점 10자리까지 저장

  class Meta:
    managed = False
    db_table = 'keyword'
