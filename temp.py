import jwt
from jwt import ExpiredSignatureError, InvalidTokenError

SECRET_KEY = "your-secret-key"  # Replace with your secret key
ALGORITHM = "HS256"

# Example JWT token (replace this with your actual token)
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxQG1vbW8uY29tIiwicm9sZSI6IkNvc3R1bWVyIiwiZXhwIjoxNzM0MzY4NzQ5fQ.KTIPkxRhAZmHxS5qrSiYdNgJ2xYjslCeDw8--mkEuPQ"

try:
    # Decode the token and verify it using the secret key and algorithm
    decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

    print("Decoded Token:", decoded_token)

except ExpiredSignatureError:
    print("Error: Token has expired.")
except InvalidTokenError:
    print("Error: Invalid token.")
