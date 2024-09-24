# Generated by Django 5.1.1 on 2024-09-20 21:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeaderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ヘッダ名')),
                ('profile_image_path', models.URLField(verbose_name='個人写真パス')),
                ('back_ground_image_path', models.URLField(verbose_name='背景写真パス')),
                ('is_active', models.BooleanField(default=False, verbose_name='有効フラグ')),
            ],
        ),
        migrations.CreateModel(
            name='MyProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_text', models.TextField(max_length=2000, verbose_name='自己紹介文')),
            ],
        ),
        migrations.CreateModel(
            name='PositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ポジション名')),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='スキルカテゴリ名')),
            ],
        ),
        migrations.CreateModel(
            name='SkillLevelModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='スキルレベル')),
            ],
        ),
        migrations.CreateModel(
            name='SkillNameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='スキル名')),
                ('description_1', models.CharField(blank=True, max_length=100, null=True, verbose_name='詳細説明1')),
                ('description_2', models.CharField(blank=True, max_length=100, null=True, verbose_name='詳細説明2')),
                ('description_3', models.CharField(blank=True, max_length=100, null=True, verbose_name='詳細説明3')),
                ('description_4', models.CharField(blank=True, max_length=100, null=True, verbose_name='詳細説明4')),
                ('description_5', models.CharField(blank=True, max_length=100, null=True, verbose_name='詳細説明5')),
            ],
        ),
        migrations.CreateModel(
            name='SkillPeriodModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='スキル使用期間')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='プロジェクト名')),
                ('back_ground', models.TextField(max_length=1000, verbose_name='背景')),
                ('overview', models.TextField(max_length=1000, verbose_name='概要')),
                ('period_from', models.DateField(verbose_name='期間開始')),
                ('period_to', models.DateField(verbose_name='期間終了')),
                ('scale', models.CharField(max_length=100, verbose_name='規模')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.positionmodel', verbose_name='ポジション名')),
                ('skill_categorys', models.ManyToManyField(related_name='projects_skill_category', to='my_profile.skillcategorymodel', verbose_name='スキルカテゴリ名')),
                ('skill_names', models.ManyToManyField(related_name='projects_skill_name', to='my_profile.skillnamemodel', verbose_name='スキル名')),
            ],
        ),
        migrations.CreateModel(
            name='SkillModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.skillcategorymodel', verbose_name='スキルカテゴリ名')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.skilllevelmodel', verbose_name='スキルレベル')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.skillnamemodel', verbose_name='スキル名')),
                ('period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_profile.skillperiodmodel', verbose_name='スキル使用期間')),
            ],
        ),
    ]
