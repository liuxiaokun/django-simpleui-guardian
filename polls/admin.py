from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Question, Choice

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




# 里面必须是数组
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
