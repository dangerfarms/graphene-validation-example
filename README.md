This example project outlines and tests a proposed interface for a validation style for Graphene.

An example implementation that supports this example can be found [here](https://github.com/dangerfarms/graphene).

Validators can be specified on any `InputObjectType` as seen in this relevant snippet:

```python
class UserInput(graphene.InputObjectType):
    username = graphene.String()
    password = graphene.String()

    def validate_password(self, password):
        if not password or len(password) < 8:
            raise GraphQLError('Please enter a password at least eight characters long')
```

## Why?

This approach co-locates input shapes with their appropriate validation and discourages repeated logic
(and minimises forgotten validation steps within mutation functions).

## Why not?

The existing feature set of Graphene is tightly coupled to GraphQL, with an obvious 1-to-1 mapping from the Graphene schema to the resulting core GraphQL schema.
This validation interface is in no way standard to Graphene and such non-standard approaches have downsides:
1. They can mislead newcomers to the GraphQL ecosystem by blurring the line between GraphQL specification, and _implementations_ of the GraphQL specification like Graphene.
2. They open the door to further deviation from the GraphQL specs, raising the question of where to draw the line.

## Running

1. Clone this repo.
2. Create a virtualenv: `python3 -m venv venv`
3. Source the virtualenv: `source venv/bin/activate`
4. Run the tests: `python -m unittest`
