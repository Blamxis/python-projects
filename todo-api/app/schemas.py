from pydantic import BaseModel, ConfigDict

class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    completed: bool

class TodoOut(TodoBase):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
