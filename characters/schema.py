import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Character, Film, Planet

class CharacterNode(DjangoObjectType):
    class Meta:
        model = Character
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'films': ['exact', 'icontains'],
        }
        interfaces = (relay.Node, )

class CreateCharacter(graphene.Mutation):
    class Input:
        name = graphene.String()
        films = graphene.String(required=False)
    name = graphene.Field(CharacterNode)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        #films = kwargs.get('films', '').strip()
        obj = Character.objects.create(name=name)
        return CreateCharacter(name=obj)

class FilmNode(DjangoObjectType):
    class Meta:
        model = Film
        # Allow for some more advanced filtering here
        filter_fields = {
            'film_title': ['exact', 'icontains', 'istartswith'],
            'director': ['exact', 'icontains', 'istartswith'],
            'producer': ['exact', 'icontains', 'istartswith'],
            'opening_crawl': ['exact', 'icontains', 'istartswith'],
            'planets': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class CreateFilm(graphene.Mutation):
    class Input:
        film_title = graphene.String()
        director = graphene.String(required=False)
        producer = graphene.String(required=False)
        opening_crawl = graphene.String(required=False)
        planets = graphene.String(required=False)

    film_title = graphene.Field(FilmNode)

    @staticmethod
    def mutate(root, info, **kwargs):
        film_title = kwargs.get('film_title', '').strip()
        director = kwargs.get('films', '').strip()
        producer = kwargs.get('producer', '').strip()
        opening_crawl = kwargs.get('opening_crawl', '').strip()
        # planets = kwargs.get('planets', '').strip()

        obj = Film.objects.create(film_title=film_title, director=director, producer=producer,
        opening_crawl = opening_crawl
        )
        return CreateFilm(film_title=obj)

class PlanetNode(DjangoObjectType):
    class Meta:
        model = Planet
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )

class CreatePlanet(graphene.Mutation):
    class Input:
        name = graphene.String()
    name = graphene.Field(PlanetNode)

    @staticmethod
    def mutate(root, info, **kwargs):
        name = kwargs.get('name', '').strip()
        obj = Planet.objects.create(name=name)
        return CreatePlanet(name=obj)


class Query(graphene.ObjectType):
    character = relay.Node.Field(CharacterNode)
    all_characters = DjangoFilterConnectionField(CharacterNode)

    film = relay.Node.Field(CharacterNode)
    all_films = DjangoFilterConnectionField(CharacterNode)

    planet = relay.Node.Field(PlanetNode)
    all_planets = DjangoFilterConnectionField(PlanetNode)

class Mutation(graphene.ObjectType):
    create_character = CreateCharacter.Field()
    create_film = CreateFilm.Field()
    create_planet = CreatePlanet.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)