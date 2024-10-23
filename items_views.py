from fastapi import Path, APIRouter
from typing import Annotated

router = APIRouter(prefix="/items", tags=["Items"])
db_info = [
    1, 2, 3, 4, 5, 6
]


@router.get("/last/")
async def last_item():
    return {"item1": db_info[-1]}


@router.get("/{item_id}/")
async def get_itemid(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {"item_id": item_id}
