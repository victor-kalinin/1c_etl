from pydantic import BaseModel


class TemplateModel(BaseModel):
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
