from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from .models import Product


async def get_all_products(session: AsyncSession):
    result = await session.execute(select(Product))
    return result.scalars().all()


async def get_product_by_id(session: AsyncSession, product_id: int):
    result = await session.execute(
        select(Product).where(Product.id == product_id)
    )
    return result.scalar_one_or_none()


async def create_product(
        session: AsyncSession,
        name: str,
        price: float,
        quantity: int
):
    product = Product(name=name, price=price, quantity=quantity)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(session: AsyncSession, product_id: int, **kwargs):
    await session.execute(
        update(Product).where(Product.id == product_id).values(**kwargs)
    )
    await session.commit()


async def delete_product(session: AsyncSession, product_id: int):
    await session.execute(delete(Product).where(Product.id == product_id))
    await session.commit()
