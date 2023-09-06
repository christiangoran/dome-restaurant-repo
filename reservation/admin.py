from django.contrib import admin
from .models import Reservation, Table
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialAccount, SocialApp, SocialToken

admin.site.register(Reservation)
admin.site.register(Table)

# The following lines are added to remove the default django admin apps
admin.site.unregister(Site)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(SocialToken)