from django import template

register = template.Library()

@register.filter('fieldtype')
def fieldtype(field):
	return field.field.widget.__class__.__name__

@register.assignment_tag
def define(val=None):
	return val
