# schemas/token.py
from pydantic import BaseModel

# Token schema (for the token response)
class Token(BaseModel):
    access_token: str
    token_type: str

# Token data schema (for extracting user data from the token)
class TokenData(BaseModel):
    username: str
    role: str