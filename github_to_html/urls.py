from django.conf.urls import patterns, include, url
from github_to_html.views import JSONGithubToHtmlView, HtmlGithubToHtmlView

urlpatterns = patterns('',
    url(r'^/html/(?P<paths>.*)$', JSONGithubToHtmlView.as_view()),
    url(r'^/view/(?P<paths>.*)$', HtmlGithubToHtmlView.as_view()),
)
