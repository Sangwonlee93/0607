from django.db import models
from member.models import Member

# Model을 admin site에 등록
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField('카테고리 이름', max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='카테고리',on_delete=models.CASCADE)
    title = models.CharField('제목', max_length=255)
    subtitle = models.CharField('부제목', max_length=255)
    content = models.TextField('내용')
    is_deleted = models.BooleanField('삭제된 글', default=False)
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    deleted_at = models.DateTimeField('삭제일', default=None, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    member = models.ForeignKey(Member, verbose_name='작성자',on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='원본글',on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용', help_text='댓글 내용입니다.')
    report_count = models.IntegerField('신고수')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    is_blocked = models.BooleanField('노출 제한', default=False)

    def __str__(self):
        return self.content

