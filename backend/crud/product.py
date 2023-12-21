from typing import Type
from crud.base import CRUDBase, ProductCRUD, ProductImageCRUD
from schemas import ProductById, ProductCreate, ProductUpdate, CategoryById, CategoryCreate, CategoryUpdate, ProductImageById, ProductImageCreate, ProductImageUpdate
from models import Product, Category, ProductImage, ProductOption, Option


class CRUDProduct(CRUDBase[ProductById, ProductCreate, ProductUpdate]):
    pass

class CRUDProduct_Type(ProductCRUD):
    pass

class CRUDCategory(CRUDBase[CategoryById, CategoryCreate, CategoryUpdate]):
    pass

class CRUDProductImage(CRUDBase[ProductImageById, ProductImageCreate, ProductUpdate]):
    pass

class CRUDProductImage_Type(ProductImageCRUD):
    pass

class CRUDCategory_Type(ProductCRUD):
    pass

class CRUDProductOption(CRUDBase[ProductById, ProductCreate, ProductUpdate]):
    pass

class CRUDProductOption_Type(ProductCRUD):
    pass

class CRUDOption(CRUDBase[ProductById, ProductCreate, ProductUpdate]):
    pass

class CRUDOption_Type(ProductCRUD):
    pass


product = CRUDProduct(Product)
productInteract = CRUDProduct_Type(Product)
category = CRUDCategory(Category)
categoryInteract = CRUDCategory(Category)
productImage = CRUDProductImage(ProductImage)
productImageInteract = CRUDProductImage(ProductImage)
