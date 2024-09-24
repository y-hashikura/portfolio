from django.contrib import admin
from .models import (
    SkillModel, 
    HeaderModel, 
    MyProfileModel, 
    ProjectModel, 
    PositionModel, 
    SkillNameModel, 
    SkillLevelModel, 
    SkillPeriodModel, 
    SkillCategoryModel,
    MyHistoryModel,
    MyHistoryNameModel,
    MenuModel,
)

# Register your models here.
admin.site.register(SkillModel)
admin.site.register(HeaderModel)
admin.site.register(MyProfileModel)
admin.site.register(ProjectModel)
admin.site.register(PositionModel)
admin.site.register(SkillNameModel)
admin.site.register(SkillLevelModel)
admin.site.register(SkillPeriodModel)
admin.site.register(SkillCategoryModel)
admin.site.register(MyHistoryModel)
admin.site.register(MyHistoryNameModel)
admin.site.register(MenuModel)
