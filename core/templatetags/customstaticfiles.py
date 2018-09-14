from urllib.parse import urljoin, quote, urlparse, parse_qsl, urlencode, urlunparse
from django.apps import apps
from django import template
from django.templatetags.static import StaticNode, PrefixNode
from project.settings import STATIC_VERSION

register = template.Library()


class CustomStaticNode(StaticNode):
	@classmethod
	def handle_simple(cls, path):
		static_url = urljoin(PrefixNode.handle_simple("STATIC_URL"), quote(path))

		# Adding static version to url
		params = {'v': STATIC_VERSION}

		url_parts = list(urlparse(static_url))
		query = dict(parse_qsl(url_parts[4]))
		query.update(params)

		url_parts[4] = urlencode(query)
		static_url = urlunparse(url_parts)
		# End Adding static version to url

		return static_url

	@classmethod
	def handle_token(cls, parser, token):
		"""
		Class method to parse prefix node and return a Node.
		"""
		bits = token.split_contents()

		if len(bits) < 2:
			raise template.TemplateSyntaxError(
				"'%s' takes at least one argument (path to file)" % bits[0])

		path = parser.compile_filter(bits[1])

		if len(bits) >= 2 and bits[-2] == 'as':
			varname = bits[3]
		else:
			varname = None

		return cls(varname, path)


@register.tag('static')
def do_static(parser, token):
	"""
	Joins the given path with the STATIC_URL setting.

	Usage::

		{% static path [as varname] %}

	Examples::

		{% static "myapp/css/base.css" %}
		{% static variable_with_path %}
		{% static "myapp/css/base.css" as admin_base_css %}
		{% static variable_with_path as varname %}

	"""
	return CustomStaticNode.handle_token(parser, token)


def static(path):
	return CustomStaticNode.handle_simple(path)
