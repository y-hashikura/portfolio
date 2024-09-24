"""
ポートフォリオ関連のモデル群を管理するモジュール
"""

from django.db import models

class HeaderModel(models.Model):
    """
    ヘッダー情報を管理するモデル
    """
    name = models.CharField(max_length=100, verbose_name="ヘッダ名")
    profile_image_path = models.URLField(verbose_name="個人写真パス")
    back_ground_image_path = models.URLField(verbose_name="背景写真パス")
    is_active = models.BooleanField(default=False, verbose_name="有効フラグ")
    
    def __str__(self):
        return self.name

class MyProfileModel(models.Model):
    """
    ホーム情報を管理するモデル
    """
    profile_text = models.TextField(max_length=2000, verbose_name="自己紹介文")
    
    def __str__(self):
        return self.profile_text

class MyHistoryNameModel(models.Model):
    """
    歴史名を管理するモデル
    """
    name = models.CharField(max_length=100, verbose_name="歴史名称")
    
    def __str__(self):
        return self.name


class MyHistoryModel(models.Model):
    """
    自分の歴史を管理するモデル
    """
    name = models.ForeignKey(MyHistoryNameModel, on_delete=models.CASCADE, verbose_name="歴史名称")
    description = models.CharField(max_length=100, verbose_name="詳細内容")
    
    def __str__(self):
        return str(self.name) + ' - ' + self.description
    
class SkillCategoryModel(models.Model):
    """
    スキルカテゴリ
    """
    name = models.CharField(max_length=100, verbose_name="スキルカテゴリ名")
    
    def __str__(self):
        return self.name

class SkillNameModel(models.Model):
    """
    スキル名
    """
    name = models.CharField(max_length=100, verbose_name="スキル名")
    description_1 = models.CharField(max_length=100, null=True, blank=True, verbose_name="詳細説明1")
    description_2 = models.CharField(max_length=100, null=True, blank=True, verbose_name="詳細説明2")
    description_3 = models.CharField(max_length=100, null=True, blank=True, verbose_name="詳細説明3")
    description_4 = models.CharField(max_length=100, null=True, blank=True, verbose_name="詳細説明4")
    description_5 = models.CharField(max_length=100, null=True, blank=True, verbose_name="詳細説明5")
    
    def __str__(self):
        return self.name

class SkillLevelModel(models.Model):
    """
    スキルレベル
    """
    # 1~5で習熟度を管理
    name = models.IntegerField(verbose_name="スキルレベル")
    
    def __str__(self):
        return str(self.name)
    
class SkillPeriodModel(models.Model):
    """
    スキル使用期間
    """
    name = models.CharField(max_length=100, verbose_name="スキル使用期間")
    
    def __str__(self):
        return self.name 

class SkillModel(models.Model):
    """
    スキルを管理するモデル
    """
    category = models.ForeignKey(SkillCategoryModel, on_delete=models.CASCADE, verbose_name="スキルカテゴリ名")
    name = models.ForeignKey(SkillNameModel, on_delete=models.CASCADE, verbose_name="スキル名")
    level = models.ForeignKey(SkillLevelModel, on_delete=models.CASCADE, verbose_name="スキルレベル")
    period = models.ForeignKey(SkillPeriodModel, on_delete=models.CASCADE, verbose_name="スキル使用期間")
    image_path = models.ImageField(upload_to="images/" , blank=True, null=True, verbose_name="ロゴ画像パス")

class PositionModel(models.Model):
    """
    ポジション
    """
    name = models.CharField(max_length=100, verbose_name="ポジション名")
    
    def __str__(self):
        return self.name 

class ProjectModel(models.Model):
    """
    プロジェクトを管理するモデル
    """
    # プロジェクト名、概要、期間、役割、技術スタック
    
    name = models.CharField(max_length=100, verbose_name="プロジェクト名")
    overview = models.TextField(max_length=1000, verbose_name="概要")
    back_ground = models.TextField(max_length=1000, verbose_name="背景")
    period_from = models.DateField(blank=True, null=True,verbose_name="期間開始")
    period_to = models.DateField(blank=True, null=True, verbose_name="期間終了")
    skill_names = models.ManyToManyField(SkillNameModel, related_name="projects_skill_name", verbose_name="スキル名")
    position = models.ForeignKey(PositionModel, on_delete=models.CASCADE, verbose_name="ポジション名")
    scale = models.CharField(max_length=100, verbose_name="規模")
    descriptions1 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容1")
    descriptions2 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容2")
    descriptions3 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容3")
    descriptions4 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容4")
    descriptions5 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容5")
    descriptions6 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容6")
    descriptions7 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容7")
    descriptions8 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容8")
    descriptions9 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容9")
    descriptions10 = models.CharField(blank=True, null=True, max_length=100, verbose_name="詳細業務内容10")
    
    def __str__(self):
        return self.name


class MenuModel(models.Model):
    """
    メニューリンクを管理するモデル
    """
    name = models.CharField(max_length=20, verbose_name="メニュー名")
    image = models.ImageField(upload_to="images/" , blank=True, null=True, verbose_name="メニュー画像")
    
    def __str__(self):
        return self.name
