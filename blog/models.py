from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Титул")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Хэш")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name="Автор")
    content = RichTextUploadingField(verbose_name="Текст")
    excerpt = models.TextField(max_length=300, help_text="Отображается под титулкой", verbose_name="Краткое описание")
    featured_image = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name="Изображение")
    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    published = models.BooleanField(default=False, verbose_name="Опубликовано")
    featured = models.BooleanField(default=False, verbose_name="На главную")

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Блог пост"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', kwargs={'slug': self.slug})


class BlogCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="Хэш")
    description = models.TextField(blank=True, verbose_name="Описание")

    class Meta:
        verbose_name_plural = "Категории блога"

    def __str__(self):
        return self.name


class BlogPostCategory(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name="Пост")
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        unique_together = ('post', 'category')
        verbose_name_plural = "Привзяка поста к категории"
