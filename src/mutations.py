import graphene
from graphql import GraphQLError


class UserInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

    def validate_password(self, password):
        if not password or len(password) < 8:
            raise GraphQLError('Please enter a password at least eight characters long')


class CreateUser(graphene.Mutation):
    class Arguments:
        user = UserInput(required=True)

    username = graphene.String()

    @staticmethod
    def mutate(root, info, user):
        return CreateUser(username=user['username'])


