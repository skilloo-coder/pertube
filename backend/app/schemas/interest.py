from pydantic import BaseModel

class InterestCreate(BaseModel):
    name: str
    description: str | None = None

class InterestResponse(BaseModel):
    id: int
    name: str
    description: str | None = None

    class Config:
        from_attributes = True
