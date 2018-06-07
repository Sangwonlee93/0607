from django.contrib import admin
from post.models import Category, Post, Comment
from django.conf.urls import url
from post.forms import MyPostAdminForm
from django.template.response import TemplateResponse
from django.contrib.admin import AdminSite
# Register your models here.
class CommentAdminSite(AdminSite):
    site_header = 'Comment administration'
class PostAdmin(admin.ModelAdmin):
    form = MyPostAdminForm
    list_per_page =10
    list_display=(
    'id','title','member','is_deleted','created_at',
    )
    list_editable=('is_deleted',)
    list_filter=(
    'member__permission','category__name','is_deleted',
    )
    fieldsets=(
    ('기본 정보',{
        'fields':(('member','category',),)
    }),
    ('제목 및 내용',{
        'fields':('title','subtitle','content',)
    }),
    ('삭제',{
        'fields':('is_deleted','deleted_at',)
    })
    )
    def get_urls(self):
        urls = super(PostAdmin, self).get_urls()
        post_urls = [
            url(r'^status/$', self.admin_site.admin_view(self.post_status_view))
        ]
        return post_urls + urls

    def post_status_view(self, request):
        context = dict(
            self.admin_site.each_context(request),
            posts=Post.objects.all()
        )
        return TemplateResponse(request, "admin/post_status.html", context)

class CommentAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Comment._meta.fields]
comment_admin = CommentAdminSite(name='comment_admin')
comment_admin.register(Comment, CommentAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
