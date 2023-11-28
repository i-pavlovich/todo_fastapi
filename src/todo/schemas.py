from pydantic import BaseModel, ConfigDict


class TaskCreationSchema(BaseModel):
    title: str
    description: str
    is_completed: bool


class TaskSchema(BaseModel):
    id: int
    title: str
    description: str
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)
