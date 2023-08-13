from typing import Annotated

from fastapi import FastAPI, Query


app = FastAPI()


@app.get("/items/")
async def read_items(
    q: Annotated[str | None, Query(
        title="Query string",
        description="Query string for the items",
        alias="item-query",
        min_length=3, max_length=50)
                 ] = ...
        ):
    results = {
        "items": [{"item_id": "Foo"},
                  {"item_id": "Bar"}]
        }
    if q:
        results.update({"q": q})
    return results


@app.get("/new_items/")
async def new_read_items(q: Annotated[list[str] | None, Query()] = None):
    query_items = {"q": q}
    return query_items
