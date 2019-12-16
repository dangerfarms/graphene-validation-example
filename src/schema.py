import graphene

from src.mutations import CreateUser


class Query(graphene.ObjectType):
    hello = graphene.String()

    def resolve_hello(self):
        return "world"


class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
