from django.contrib.sitemaps import Sitemap
from .models import Track

class TrackSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Track.objects.all()

    def lastmod(self, obj):
        return obj.updated_at
