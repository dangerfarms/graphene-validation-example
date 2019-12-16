from unittest import TestCase

from src.schema import schema


class CreateUserTestCase(TestCase):
    def test_should_succeed_when_password_is_longer_than_eight_characters(self):
        result = schema.execute(
            """
            mutation($user:UserInput!) {
                createUser(user:$user) {
                    username
                }
            }
            """,
            variables={
                'user': {
                    'username': 'user1',
                    'password': 'correct-horse'
                }
            }
        )

        self.assertEqual(result.data['createUser']['username'], 'user1')

    def test_should_return_error_when_password_is_shorter_than_eight_characters(self):
        result = schema.execute(
            """
            mutation($user:UserInput!) {
                createUser(user:$user) {
                    username
                }
            }
            """,
            variables={
                'user': {
                    'username': 'user1',
                    'password': 'horse'
                }
            }
        )

        self.assertIsNone(result.data['createUser'])
        self.assertEqual(result.errors[0].message, 'Please enter a password at least eight characters long')
