import secrets
import string


class PasswordGenerator:

    @staticmethod
    def generate_password(length=16):
        characters = (
            string.ascii_letters +
            string.digits +
            string.punctuation
        )

        while True:
            password = ''.join(
                secrets.choice(characters)
                for _ in range(length)
            )

            if (
                any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)
            ):
                return password