from django.db.models.signals import post_migrate
from datetime import date
from django.dispatch import receiver
from .models import (
    MyProfileModel,
    SkillCategoryModel, 
    SkillNameModel, 
    SkillLevelModel, 
    SkillPeriodModel,
    SkillModel, 
    PositionModel,
    MyHistoryNameModel,
    MyHistoryModel,
    MenuModel,
    ProjectModel
)

def get_skill_categorys() -> list[str]:
    """
    スキルカテゴリ取得
    """
    return [
        "バックエンド",
        "フロントエンド", 
        "データベース", 
        "フレームワーク", 
        "クラウド", 
        "管理ツール", 
        "テストツール", 
        "セキュリティ", 
        "コンテナ/仮想化", 
        "WEBサーバ", 
        "コンポーネントライブラリ", 
        "ETLツール",
        "開発エディタ",
        "OS",
        "その他"
    ]

def get_skill_names() -> list[str]:
    """
    スキル名
    """
    return [
        "Python", 
        "VB.NET", 
        "Java", 
        "PHP",
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
        "A5:SQL",
        "VSCode",
        "VS",
        "SQLServer",
        "Oracle",
        "POSTGRESQL",
        "Windows",
        "Linux",
        "CentOs",
        "Azure"
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
        1, 2, 3, 4, 5
    ]

def get_positions() -> list[str]:
    """
    ポジション
    """
    return [
        "フルスタックエンジニア", "バックエンドエンジニア", "フロントエンドエンジニア", "プロジェクトリーダ", "インフラエンジニア",
    ]

def get_my_historys() -> list[str]:
    """
    歴史
    """
    return [
        "2014年04月 大原簿記情報ビジネス専門学校 入学",
        "2016年04月 株式会社日立ソリューションズ・クリエイト (正社員)",
        "2021年10月 株式会社ファーンリッジ・ジャパン (正社員)",
        "2022年01月 テクノブレイブ株式会社 (フリーランス)",
        "2022年11月 株式会社ゲオホールディングス (フリーランス)",
        "2024年04月 青山綜合会計事務所(フリーランス)",
    ]

def get_my_menu() -> list[str]:
    """
    メニューリンク
    """
    return ["HOME", "HISTORY", "SKILL", "PROJECT"]

@receiver(post_migrate)
def initialize_data(sender, **kwargs):
    """
    マイグレーション実行後に初期データを挿入
    """
    # メニューリンク
    for menu in get_my_menu():
        MenuModel.objects.update_or_create(name=menu)
        
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
        
    # スキル一括登録
    insert_SkillModel()
        
    # ポジション
    for position in get_positions():
        PositionModel.objects.update_or_create(name=position)
        
    # 歴史名称
    for history_name in get_my_historys():
        MyHistoryNameModel.objects.update_or_create(name=history_name)
        
    # 歴史一括登録
    insert_MyHistoryModel()
    
    # 自己紹介文一括登録
    insert_MyProfileModel()
    

def insert_MyHistoryModel():
    """
    MyHisotryModelの一括登録
    """
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=1), # 大原
        description="日商簿記二級 合格"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=1), # 大原
        description="基本情報技術者試験 合格"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=1), # 大原
        description="応用情報技術者試験 合格"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=2), # 日立
        description="業務/WEBアプリケーション開発経験"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=2), # 日立
        description="要件定義、設計、実装、テスト、本番切替、運用保守の一気通貫の開発経験"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=2), # 日立
        description="主にVB.NET, ASP.NET, SQLServerで構築されたシステムの開発"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=3), # ファーンリッジ
        description="業務アプリケーション開発"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=3), # ファーンリッジ
        description="フロントエンドの開発(HTML, CSS, JavaScript等)"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=3), # ファーンリッジ
        description="バックエンドの開発(VB.NET)"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=4), # テクノブレイブ
        description="業務アプリケーション開発(VB.NET, SPREAD, SQLServer等)"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=5), # ゲオホールディングス
        description="野良アプリ(ACCESS、VBA)のSQL解析/解析仕様書の作成"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=6), # 青山
        description="Git、Githubを用いたバージョン管理経験(プル、プルリク、プッシュ、コードレビュー等)"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=6), # 青山
        description="Dockerを用いた仮想化コンテナ技術経験"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=6), # 青山
        description="Python, Streamlit, Django, RESTAPIを用いたWEBアプリケーション開発"
    )
    MyHistoryModel.objects.update_or_create(
        name=MyHistoryNameModel.objects.get(id=6), # 青山
        description="Azure App Serviceを用いたデプロイ、環境設定、githubとの自動デプロイ設定等の経験"
    )

def insert_SkillModel():
    """
    SkillModelの一括登録
    """
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="バックエンド"), 
        name=SkillNameModel.objects.get(name="Python"),
        level=SkillLevelModel.objects.get(name=3), 
        period=SkillPeriodModel.objects.get(id=3), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="バックエンド"), 
        name=SkillNameModel.objects.get(name="VB.NET"),
        level=SkillLevelModel.objects.get(name=4), 
        period=SkillPeriodModel.objects.get(id=4), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="バックエンド"), 
        name=SkillNameModel.objects.get(name="Java"),
        level=SkillLevelModel.objects.get(name=1), 
        period=SkillPeriodModel.objects.get(id=1), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="バックエンド"), 
        name=SkillNameModel.objects.get(name="PHP"),
        level=SkillLevelModel.objects.get(name=1), 
        period=SkillPeriodModel.objects.get(id=1), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フロントエンド"), 
        name=SkillNameModel.objects.get(name="JavaScript"),
        level=SkillLevelModel.objects.get(name=2), 
        period=SkillPeriodModel.objects.get(id=3), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フロントエンド"), 
        name=SkillNameModel.objects.get(name="CSS"),
        level=SkillLevelModel.objects.get(name=3), 
        period=SkillPeriodModel.objects.get(id=3), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フロントエンド"), 
        name=SkillNameModel.objects.get(name="HTML"),
        level=SkillLevelModel.objects.get(name=2), 
        period=SkillPeriodModel.objects.get(id=3), 
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フレームワーク"), 
        name=SkillNameModel.objects.get(name="BootStrap"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フレームワーク"), 
        name=SkillNameModel.objects.get(name="Django"),
        level=SkillLevelModel.objects.get(name=2), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フレームワーク"), 
        name=SkillNameModel.objects.get(name="REST API"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=2), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フレームワーク"), 
        name=SkillNameModel.objects.get(name="FastAPI"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=2), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="フレームワーク"), 
        name=SkillNameModel.objects.get(name="ASP.NET"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=4), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="クラウド"), 
        name=SkillNameModel.objects.get(name="Azure"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 1年=3年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="データベース"), 
        name=SkillNameModel.objects.get(name="SQLServer"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=4), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="データベース"), 
        name=SkillNameModel.objects.get(name="Oracle"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=1), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="データベース"), 
        name=SkillNameModel.objects.get(name="POSTGRESQL"),
        level=SkillLevelModel.objects.get(name=2), # レベル3
        period=SkillPeriodModel.objects.get(id=2), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="コンポーネントライブラリ"), 
        name=SkillNameModel.objects.get(name="SPREAD"),
        level=SkillLevelModel.objects.get(name=4), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="ETLツール"), 
        name=SkillNameModel.objects.get(name="SSIS"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=1), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="コンテナ/仮想化"), 
        name=SkillNameModel.objects.get(name="Docker"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="コンテナ/仮想化"), 
        name=SkillNameModel.objects.get(name="VMWare"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=1), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="WEBサーバ"), 
        name=SkillNameModel.objects.get(name="IIS"),
        level=SkillLevelModel.objects.get(name=1), # レベル3
        period=SkillPeriodModel.objects.get(id=1), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="管理ツール"), 
        name=SkillNameModel.objects.get(name="Backlog"),
        level=SkillLevelModel.objects.get(name=4), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="管理ツール"), 
        name=SkillNameModel.objects.get(name="Git"),
        level=SkillLevelModel.objects.get(name=4), # レベル3
        period=SkillPeriodModel.objects.get(id=4), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="管理ツール"), 
        name=SkillNameModel.objects.get(name="Github"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="OS"), 
        name=SkillNameModel.objects.get(name="Windows"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="OS"), 
        name=SkillNameModel.objects.get(name="Linux"),
        level=SkillLevelModel.objects.get(name=3), # レベル3
        period=SkillPeriodModel.objects.get(id=3), # 3年～5年未満
    )
    SkillModel.objects.update_or_create(
        category=SkillCategoryModel.objects.get(name="OS"), 
        name=SkillNameModel.objects.get(name="CentOs"),
        level=SkillLevelModel.objects.get(name=2), # レベル3
        period=SkillPeriodModel.objects.get(id=2), # 3年～5年未満
    )

def insert_MyProfileModel():
    """
    自己紹介文一括登録(最大10行)
    """
    MyProfileModel.objects.update_or_create(profile_text="はじめまして。平成8年生まれ 橋倉佳希と申します。")
    MyProfileModel.objects.update_or_create(profile_text="この度はWEB訪問頂きありがとうございます。")
    MyProfileModel.objects.update_or_create(profile_text="私は主にバックエンドエンジニアとして、業務システムやWEBアプリケーションの開発に携わってきました。")
    MyProfileModel.objects.update_or_create(profile_text="現在は、フルスタックエンジニアとしてスキルを磨くため、TypeScriptやReactの学習も並行で進めております。")
    MyProfileModel.objects.update_or_create(profile_text="また、AzureやAWS等のクラウド技術の習得にも力を入れております。")
    MyProfileModel.objects.update_or_create(profile_text="元々VB.NETによる開発が多かったのですが、スキルチェンジを図りPythonを新たに学習しており、案件に参画中です。")
