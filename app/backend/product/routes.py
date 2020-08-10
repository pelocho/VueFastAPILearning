from bson.objectid import ObjectId
from config.config import DB, CONF
from fastapi import APIRouter, Depends, HTTPException
from typing import List
import logging

from .models import ProductBase, ProductStatus, ProductOnBD

product_router = APIRouter()


def validate_object_id(id_: str):
    try:
        _id = ObjectId(id_)
    except Exception:
        if CONF['fastapi'].get('debug', False):
            logging.warning("Invalid Object ID.")
        raise HTTPException(status_code=400)
    return _id


async def _get_product_or_404(id_: str):
    _id = validate_object_id(id_)
    product = await DB.product.find_one({'_id': _id})
    if product:
        product['id_'] = str(product['_id'])
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


def fic_product_id(product):
    product['id_'] = str(product['_id'])
    return product


@product_router.get('/', response_model=List[ProductOnBD])
async def get_all_products(status: ProductStatus = None, limit: int = 10, skip: int = 0):
    if status is None:
        products_cursor = DB.product.find().skip(skip).limit(limit)
    else:
        products_cursor = DB.product.find({'status': status.value}).skip(skip).limit(limit)
    products = await products_cursor.to_list(length=limit)
    return list(map(fic_product_id, products))


@product_router.post('/', response_model=ProductOnBD)
async def add_product(product: ProductBase):
    product_op = await DB.product.insert_one(product.dict())
    if product_op.inserted_id:
        product = await _get_product_or_404(product_op.inserted_id)
        product['id_'] = str(product['_id'])
        return product


@product_router.get('/{id_}', response_model=ProductOnBD)
async def get_product_by_id(id_: ObjectId = Depends(validate_object_id)):
    product = await DB.product.find_one({'_id': id_})
    if product:
        product['id_'] = str(product['_id'])
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found")


@product_router.delete('/{id_}', dependencies=[Depends(_get_product_or_404)], response_model=dict)
async def delete_product_by_id(id_: str):
    product_op = await DB.product.delete_one({'_id': ObjectId(id_)})
    if product_op.deleted_count:
        return {'status': f'deleted count: {product_op.deleted_count}'}


@product_router.put('/{id_}', dependencies=[Depends(validate_object_id), Depends(_get_product_or_404)],
                    response_model=ProductOnBD)
async def update_product(id_: str, product_data: ProductBase):
    product_op = await DB.product.update_one(
        {'_id': ObjectId(id_)}, {'$set': product_data.dict()}
    )
    if product_op.modified_count:
        return await _get_product_or_404(id_)
    else:
        raise HTTPException(status_code=304)
