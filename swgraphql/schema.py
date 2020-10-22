import graphene

import characters.schema

from graphene_django.debug import DjangoDebug


class Query(
    characters.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    debug = graphene.Field(DjangoDebug, name="_debug")

class Mutation(
    characters.schema.Mutation,
    graphene.ObjectType
    ):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)