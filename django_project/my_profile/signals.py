from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import (
    SkillCategoryModel, 
    SkillNameModel, 
    SkillLevelModel, 
    SkillPeriodModel, 
    PositionModel,
    MyHistoryNameModel,
    MenuModel
)

def get_skill_categorys() -> list[str]:
    """
    スキルカテゴリ取得
    """
    return [
        "言語", 
        "DB", 
        "FW", 
        "クラウド", 
        "バージョン管理", 
        "テストツール", 
        "セキュリティ", 
        "コンテナ/仮想化", 
        "WEBサーバ", 
        "コンポーネントライブラリ", 
        "ETLツール"
    ]

def get_skill_names() -> list[str]:
    """
    スキル名
    """
    return [
        "Python", 
        "VB.NET", 
        "Java", 
        "HTML", 
        "CSS", 
        "ASP.NET",
        "React", 
        "JavaScript",
        "BootStrap", 
        "SPREAD", 
        "SSIS",  
        "Docker",
        "VMWare",
        "IIS",
        "TEAMS",
        "ZOOM",
        "Slack",
        "Backlog",
        "Git",
        "Github",
        "Django", 
        "REST API", 
        "FastAPI", 
        "ASP.NET", 
    ]

def get_skill_periods() -> list[str]:
    """
    スキル使用期間
    """
    return [
        "半年未満", "半年以上~1年未満", "1年以上~3年未満", "3年以上~5年未満", "5年以上"
    ]

def get_skill_levels() -> list[str]:
    """
    スキルレベル
    """
    return [
        "初級", "中級", "上級"
    ]

def get_positions() -> list[str]:
    """
    ポジション
    """
    return [
        "PG", "SE", "PL", "PM", "QA"
    ]

def get_my_historys() -> list[str]:
    """
    歴史
    """
    return [
        "2014年04月 大原簿記情報ビジネス専門学校 入学",
        "2016年04月 株式会社日立ソリューションズ・クリエイト (正社員)",
        "2021年10月 株式会社ファーンリッジ・ジャパン (正社員)"
        "2022年01月 テクノブレイブ株式会社 (フリーランス)",
        "2022年11月 株式会社ゲオホールディングス (フリーランス)",
        "2024年04月 青山綜合会計事務所(フリーランス)",
    ]

def get_my_menu() -> list[str]:
    """
    メニューリンク
    """
    return ["HOME", "HISTORY", "SKILL", "PROJECT", "ADMIN"]

@receiver(post_migrate)
def initialize_data(sender, **kwargs):
    """
    マイグレーション実行後に初期データを挿入
    """
    # スキルカテゴリ登録
    for category in get_skill_categorys():
        SkillCategoryModel.objects.update_or_create(name=category)
    
    # スキル名登録
    for name in get_skill_names():
        SkillNameModel.objects.update_or_create(name=name)
    
    # スキル使用期間登録
    for period in get_skill_periods():
        SkillPeriodModel.objects.update_or_create(name=period)
    
    # スキルレベル
    for level in get_skill_levels():
        SkillLevelModel.objects.update_or_create(name=level)
        
    # ポジション
    for position in get_positions():
        PositionModel.objects.update_or_create(name=position)
        
    # 歴史名称
    for history_name in get_my_historys():
        MyHistoryNameModel.objects.update_or_create(name=history_name)
        
    # メニューリンク
    for menu in get_my_menu():
        MenuModel.objects.update_or_create(name=menu)