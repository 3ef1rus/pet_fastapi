from fastapi import APIRouter, status, Depends
from .schemas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial
from . import crud
from core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import product_by_id
router = APIRouter(tags=["Products"])


@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scope_session_dependency)
):

    return await crud.get_products(session=session)


@router.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_create: ProductCreate,
    session: AsyncSession = Depends(db_helper.scope_session_dependency)
):

    return await crud.create_product(session=session, product_create=product_create)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id)
):
    return product


@router.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),

):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update
    )


@router.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scope_session_dependency),

):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True
    )


@router.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def detele_product(
    session: AsyncSession = Depends(db_helper.scope_session_dependency),
    product: Product = Depends(product_by_id),
) -> None:
    return await crud.delete_product(
        session=session,
        product=product
    )
