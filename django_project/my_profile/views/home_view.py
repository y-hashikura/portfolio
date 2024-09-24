"""
ポートフォリオメイン画面のビューモジュール
"""
from typing import Any
from django.views.generic import TemplateView
from ..models import MyHistoryModel, SkillModel, MenuModel
from itertools import zip_longest
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
            
        context["skills"] = SkillModel.objects.all()
        
        # メニューリンク情報取得
        menus = MenuModel.objects.all()
        result = []
        for menu in menus:
            result.append((menu.name, menu.image))
        context["menu"] = result
        
        
        
        # サンプルデータ
        projects = [
            {'name': 'プロジェクトA', 'description': 'ウェブアプリ開発プロジェクト', 'language': 'Python, JavaScript', 'position': 'バックエンドエンジニア', 'size': 10},
            {'name': 'プロジェクトB', 'description': 'モバイルアプリ開発プロジェクト', 'language': 'Swift, Kotlin', 'position': 'フロントエンドエンジニア', 'size': 5},
            {'name': 'プロジェクトC', 'description': 'データ分析プロジェクト', 'language': 'R, Python', 'position': 'データサイエンティスト', 'size': 3},
            {'name': 'プロジェクトD', 'description': 'クラウドインテグレーションプロジェクト', 'language': 'AWS, Python', 'position': 'クラウドエンジニア', 'size': 8},
            {'name': 'プロジェクトE', 'description': 'AI開発プロジェクト', 'language': 'Python, TensorFlow', 'position': 'リードエンジニア', 'size': 12},
            {'name': 'プロジェクトF', 'description': '機械学習プロジェクト', 'language': 'Python, Scikit-learn', 'position': 'データサイエンティスト', 'size': 6},
            # 他のプロジェクトをここに追加...
        ]
        
        args = [iter(projects)] * 3

        context["chunked_projects"] = list(zip_longest(*args))
        
        context["context"] = context
        
        return context