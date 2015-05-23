# -*- coding: UTF-8 -*-
from django import template
from blog.models import Post, Comment
register=template.Library()
 
@register.inclusion_tag('blog/lastnews.html') # регистрируем тег и подключаем шаблон lastnews_tpl.html из папки newslist
def lastnews():
    return {
		'last3news': Post.objects.filter(status='1')[:3],
	}
    