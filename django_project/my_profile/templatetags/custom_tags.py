from django import template
from django.template.loader import get_template
from django.template.loader import render_to_string
from django.template.exceptions import TemplateDoesNotExist
register = template.Library()

@register.simple_tag
def render_dynamic_template(name, context_data: dict =None):
    template_name = f'my_profile/portfolio/{name}.html'
    try:
        # 渡されたテンプレート名でテンプレートをレンダリング
        return render_to_string(template_name, context_data )
    except TemplateDoesNotExist:
        # テンプレートが見つからない場合、デフォルトテンプレートを使用
        return render_to_string('my_profile/portfolio/default.html', context_data )


@register.filter
def range_filter(start, end):
    """
    指定された範囲のリストを返すカスタムフィルタ
    """
    return range(start, end)

@register.filter
def to_int(value):
    """文字列を整数に変換するフィルタ"""
    return int(value)

@register.simple_tag
def get_test_projects():
    # プロジェクト辞書のサンプルデータを返す
    projects = [
        {
            'name': 'プロジェクトA',
            'description': 'ウェブアプリ開発プロジェクト',
            'language': 'Python, JavaScript',
            'position': 'バックエンドエンジニア',
            'size': 10,
        },
        {
            'name': 'プロジェクトB',
            'description': 'モバイルアプリ開発プロジェクト',
            'language': 'Swift, Kotlin',
            'position': 'フロントエンドエンジニア',
            'size': 5,
        },
        {
            'name': 'プロジェクトC',
            'description': 'データ分析プロジェクト',
            'language': 'R, Python',
            'position': 'データサイエンティスト',
            'size': 3,
        },
    ]
    return projects