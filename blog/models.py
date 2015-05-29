from django.db import models
from django.contrib.auth.models import User
from utils import helpers

''' Types '''

BLOG_ITEM_STATUS = (
        ('0', 'Draft'),
        ('1', 'Published'),
        ('2', 'Not Published'),
)

def get_blog_file_name(instance, filename):
    return helpers.get_file_filename(instance, filename, "blog")

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

class Page(models.Model):
    status = models.CharField(max_length=1, choices=BLOG_ITEM_STATUS, default='0')
    title = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, editable=True)
    content = models.TextField()
#    widgets = models.ManyToManyField(Widget, null=True, blank=True)
    featured_image = models.ImageField(max_length=1024, null=True, blank=True, upload_to=get_blog_file_name)
#    related_slider = models.ForeignKey(Slider, null=True, blank=True)

    def __str__(self):
        return u"{}".format(self.title)

    def __unicode__(self):
        return self.__str__()

#    def get_widgets(self):
#        return self.widgets.all()

#    def save(self, *args, **kwargs):
#        self.slug = helpers.get_slug(self.title)
#        super(Page, self).save(*args, **kwargs)
