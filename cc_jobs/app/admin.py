from django.contrib import admin
from . import models
from embed_video.admin import AdminVideoMixin

# Register your models here.
# class ArticleAdmin(admin.ModelAdmin):
#     list_display=['title','slug','status']
#     search_fields =('title','body',)
#     list_filter=('title','body',)
#     fieldsets = [('Description', {'fields': ['title','slug','body','thumb','status']}), ]
#     actions=['make_approved',]
#
#
#     def make_approved(self, request, queryset):
#         rows_updated = queryset.update(status='a')
#         if rows_updated == 1:
#              message_bit = "1 story was"
#         else:
#              message_bit = "%s stories were" % rows_updated
#         self.message_user(request, "%s successfully marked as published." % message_bit)
#     make_approved.short_description='Approve'







class ActivityAdmin(AdminVideoMixin,admin.ModelAdmin):
    list_display=['name','image','description','date_happen']
    search_fields =('name','image','description','date_happen')
    list_filter=('name','image','description','date_happen')


admin.site.register(models.Activity,ActivityAdmin)
