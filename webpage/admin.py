from django.contrib import admin
from .models import UserDetail, ToolStack, TechStack, Projects
# Register your models here.


class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'profile', 'user_mail')
    list_display_links = ('user_mail', 'profile', 'user_mail')


class techAdmin(admin.ModelAdmin):
    list_display = ('id', 'technology', 'experience',)
    list_display_links = ('technology', 'experience',)


class toolAdmin(admin.ModelAdmin):
    list_display = ('id', 'tool_soft', 'tool_experience',)
    list_display_links = ('tool_soft', 'tool_experience',)


class projAdmin(admin.ModelAdmin):
    list_display = ('id', 'proj_name', )
    list_display_links = ('proj_name', )


admin.site.register(UserDetail, userAdmin)
admin.site.register(TechStack, techAdmin)
admin.site.register(ToolStack, toolAdmin)
admin.site.register(Projects, projAdmin)
