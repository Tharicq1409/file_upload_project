from django.urls import path
from .  import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.application,name = "applynow"),
    path('autocomplete/',views.autocomplete,name = "autocomplete"),
    path('city-autocomplete/',views.city_auto,name = 'city-autocomplete'),
    path('state-autocomplete',views.state_auto,name = 'state-autocomplete'),
]
'''
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

