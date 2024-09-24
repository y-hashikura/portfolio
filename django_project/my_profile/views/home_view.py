"""
ポートフォリオメイン画面のビューモジュール
"""
from typing import Any
from django.views.generic import TemplateView
from ..models import MyHistoryModel, SkillModel, MenuModel

from collections import defaultdict

class HomeView(TemplateView):
    template_name = "my_profile/base/base.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # 歴史情報取得
        histories = MyHistoryModel.objects.all()
        result = defaultdict(list)
        for history in histories:
            result[history.name].append(history.description)    
        context["histories"] = dict(result)
        
        # スキル情報取得
        skills = SkillModel.objects.all()
        result = {}
        for row in skills:
            if row.category not in result:
                result[row.category] = {}
            
            result[row.category][row.name] = row.image_path
        
        context["skills"] = result
        
        # メニューリンク情報取得
        menus = MenuModel.objects.all()
        result = []
        for menu in menus:
            result.append((menu.name, menu.image))
        context["menu"] = result
        
        context["context"] = context
        
        return context