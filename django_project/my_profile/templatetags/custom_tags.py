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