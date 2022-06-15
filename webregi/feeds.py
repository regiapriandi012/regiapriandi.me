from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed


class LatestPostsFeed(Feed):
    title = "Regi Apriandi Blog"
    link = "/amp/blog/"
    description = "Posts of Regi Apriandi Blog"

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

    def item_link(self, item):
        return reverse("post_detail_amp", args=[item.slug])

from django.utils.feedgenerator import Atom1Feed

class AtomSiteNewsFeed(LatestPostsFeed):
    feed_type = Atom1Feed
    subtitle = LatestPostsFeed.description
