"""
This script defines the format of the input data
accepted by the API for validation
"""

#Import library
from pydantic import BaseModel, Field

#Create class for data validation
class StockFields(BaseModel):
    open: float = Field(gt=0)
    high: float = Field(gt=0)
    low: float = Field(gt=0)
    close: float = Field(gt=0)
    adj_close: float = Field(gt=0)
    volume: float = Field(gt=0)
