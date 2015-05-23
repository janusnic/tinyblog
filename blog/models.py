from django.db import models
from django.contrib.auth.models import User

BLOG_ITEM_STATUS = (
        ('0', 'Draft'),
        ('1', 'Published'),
        ('2', 'Not Published'),
)

class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	slug = models.SlugField(unique=True)

	def __str__(self):
		return self.name

class Post(models.Model):
	category = models.ForeignKey(Category)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=128)
	slug = models.SlugField(unique=True)
	body = models.TextField()
	url = models.URLField(blank=True)
	views = models.IntegerField(default=0)
	status = models.CharField(max_length=1, choices=BLOG_ITEM_STATUS, default='0')
	updated = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['created']

	def __str__(self):
		return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __str__(self):
        return self.user.username

class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    body = models.TextField()
    post = models.ForeignKey(Post)

    def __str__(self):
        return str("%s: %s" % (self.post, self.body[:60]))