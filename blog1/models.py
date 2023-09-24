from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, 'Draft'),(1,'Published'))


class BlogPosts(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=255, unique=True)
    updated_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    main_image = CloudinaryField('image', default='placeholder')
    snippet_text = models.TextField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    publish_status = models.IntegerField(choices=STATUS, default=0)
    post_likes = models.ManyToManyField(User, related_name='blog-likes', blank=True)

    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.post_likes.count()


class Comment(models.Model):
    post = models.ForeignKey(BlogPosts, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_on')

    def __str__(self):
        return f"The comment {self.body} by {self.name} left on {self.created_on}"

        






