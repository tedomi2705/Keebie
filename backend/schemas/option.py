from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class OptionBase(BaseModel):
    category_id: int
    category_type: str
    option_name: str
    in_stock: int
    
class OptionById(OptionBase):
    id: int
    
    class Config:
        from_attributes = True
        
class OptionCreate(OptionBase):
    pass

class OptionUpdate:
    pass

class ProductOptionBase(BaseModel):
    product_id: int
    option_id: int
    addition_price: float
    
class ProductOptionById(ProductOptionBase):
    id: int
    
    class Config:
        from_attributes = True
        
class ProductOptionCreate(ProductOptionBase):
    pass

class ProductOptionUpdate:
    pass