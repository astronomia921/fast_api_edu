from pydantic import BaseModel


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
                }
            }


class Item(BaseModel):
    item: TodoItem
    status: str


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": Item
            }
        }
