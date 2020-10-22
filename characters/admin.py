from django.conf.urls import url, include
from django.contrib import admin

from characters.models import (Character, Film, Planet)

#from characters.views import GraphQLView

#from swgraphql.schema import schema

# Register your models here.

@admin.register(Character)
class CharactersAdmin(admin.ModelAdmin):
    pass

@admin.register(Film)
class FilmsAdmin(admin.ModelAdmin):
    pass

@admin.register(Planet)
class PlanetsAdmin(admin.ModelAdmin):
    pass

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^graphql$', GraphQLView.as_view(graphiql=True, schema=schema)),
]
