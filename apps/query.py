from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"}
]


@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description":
                    "This is an amazing item that has a long description"
                    }
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {
                "description":
                    "This is an amazing item that has a long description"
                }
        )
    return item


class ModelName(BaseModel):
    item_id: str
    needy: str
    skip: int = 0
    limit: int | None = None


@app.get("/items/{item_id}")
async def new_read_user_item(model_name: ModelName):
    item = {
        "item_id": model_name.item_id,
        "needy": model_name.needy,
        "skip": model_name.skip,
        "limit": model_name.limit
    }
    return item

# needy, обязательный str
# skip, типа int и со значением по умолчанию 0
# limit, необязательный int
