from pydantic import BaseModel

class PhoneRecord(BaseModel):
    name : str
    phone_number : str
    email : str | None = None


class UpdatePhoneRecord(BaseModel):
    name : str | None = None
    phone_number : str | None = None
    email : str | None = None    