from django.conf.urls.defaults import *
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView

from post.views import ListPostView, DateDetailPostView, \
    PostsByTagView, DraftPostView, RedirectPostView, PostsByCategoryView, \
    PostsByAuthorView, SubmittedArticleListView
from post.feeds import LatestEntriesFeed

urlpatterns = patterns('post.views',
    # List view for all published posts
    url(r'^$', ListPostView.as_view(),name='post_list'),
    
    # Detail view for post by date and slug
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[a-zA-Z0-9-_]+)/$', 
       DateDetailPostView.as_view(), name='post_detail'),

    
    # Detail view for post by id
    url(r'^id/(?P<pk>\d+)/$', 
        RedirectPostView.as_view(), name='story_id_detail'),
    
    # Detail view for unpublished post 
    url(r'^draft/(?P<pk>\d+)/$',
        permission_required('post.change_basicpost')
        (DraftPostView.as_view()), name='post_draft_detail'),

    # RSS feed for posts 
    url(r'^feed/$', LatestEntriesFeed(), name='post_feed'),
    
    # List view by tag
    url(r'^tag/(?P<tag>[\"\w\" \-]+)/$', PostsByTagView.as_view(), name='post_tag_list'),

    url(r'^category/(?P<category>[\"\w\" \-]+)/$', PostsByCategoryView.as_view(), name='post_category_list'),
    
    url(r'^author/(?P<author>\d+)/$', PostsByAuthorView.as_view(), name='post_author_list'),
    
    url(r'^submit/list/$', SubmittedArticleListView.as_view(), name='submit_article_list'),
    url(r'^submit/add/$', 'submit_article', name='submit_article'),
    url(r'^submit/success/$', TemplateView.as_view(template_name="submit_article/success.html"), name='submit_article_success'),
    
    url(r'^clearcache/$', 'clear_cache', name='clear_cache'),

    url(r'^print/(?P<slug>[a-zA-Z0-9-_]+)/$', 'print_post', name='print_post'),

    # Preview for Markdown for enhanced text fields
    (r'^markdownpreview/$', 'markdownpreview'),
)

