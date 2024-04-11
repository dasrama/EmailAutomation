from pydantic import BaseModel


class EmailRequest(BaseModel):
    receiver: str
    email_username: str
    email_password: str