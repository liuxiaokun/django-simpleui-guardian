from import_export import resources
from .models import Question


class QuestionResource(resources.ModelResource):
    class Meta:
        model = Question
        # 要导出的字段
        fields = (
            "question_text",
        )
        # 导出的字段的排序
        export_order = (
            "question_text",
        )

