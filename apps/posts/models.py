from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.utils.safestring import mark_safe
from unidecode import unidecode
from django.db.models.signals import pre_save, pre_delete
from markdown2 import markdown


class Tag(models.Model):
    name = models.CharField('标签名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    另外一个表,储存文章的分类信息
    文章表的外键指向
    """
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)

    def __str__(self):
        return self.name


# 博客文章
class Post(models.Model):
    title = models.CharField('标题', max_length=50)
    context = models.TextField('正文')
    slug = models.SlugField(unique=True, null=True, verbose_name='浏览器地址')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞量', default=0)
    topped = models.BooleanField('顶置', default=False)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    category = models.ForeignKey(
        Category, verbose_name='所属分类', on_delete=models.SET_NULL, null=True)

    # image = models.ImageField(null=True,blank=True)   #TODO: 上传图片

    def ___str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={"slug", self.slug})

    def get_markdown(self):
        context = self.context
        return mark_safe(markdown(context))


def create_slug(instance, new_slug=None):
    slug = slugify(unidecode(instance.title))
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    if qs.exists():
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug)
    return slug


def pre_save_subscriber(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


def post_delete_subscriber(sender, instance, *args, **kwargs):
    if instance.image:
        instance.image.delete(False)


pre_save.connect(pre_save_subscriber, Post)
pre_delete.connect(pre_save_subscriber, Post)


class Comment(models.Model):
    user_name = models.CharField('评论者姓名', max_length=100)
    body = models.TextField('评论内容')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='所属文章')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.body[:20]  # 返回前20个字符串
