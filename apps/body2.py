from typing import Annotated

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field, HttpUrl
app = FastAPI()


class Image(BaseModel):
    url: HttpUrl
    name: str


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="The description of the item", max_length=300
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero")
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    results = {
        "item_id": item_id,
        "item": item,
        "user": user,
        "importance": importance
        }
    return results


@app.put("/items/{item_id}")
async def update_item_new(
        item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
# -->
# {
#     "item": {
#         "name": "Foo",
#         "description": "The pretender",
#         "price": 42.0,
#         "tax": 3.2
#     }
# }


@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
