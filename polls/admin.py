from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Question, Choice

admin.site.site_header = '华东投票管理'
admin.site.site_title = '投票管理'
admin.site.index_title="名字"


class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(GuardedModelAdmin):
    # 可为1对多条件的进行一次性添加
    inlines = [ChoiceInline]
    # 设置列表显示
    list_display = ['question_text', 'pub_date']
    # 设置每页的记录数， 默认100条
    list_per_page = 10

class ChoiceAdmin(GuardedModelAdmin):
    # 设置列表显示
    list_display = ['choice_text', 'votes']
    # 设置每页的记录数， 默认100条
    list_per_page = 10
    # 排序
    ordering = ['-votes']
    # 默认可编辑字段
    list_editable = ['votes']
    # 可进行过滤的字段
    list_filter = ['votes']
    # 搜索
    search_fields = ['choice_text']




# 里面必须是数组
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
