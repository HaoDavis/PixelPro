# 应用目录中的templatetags/custom_filters.py

from django import template

register = template.Library()


# 自定义过滤器函数
@register.filter(name='getDictVal')
def get_dict_val(m, k):
    return m[k]
