# product.py

import abc
from datetime import datetime, date
from typing import Dict


# Custom Exceptions
class InventoryError(Exception):
    """Base exception for inventory-related errors"""
    pass

class InsufficientStockError(InventoryError):
    pass

class DuplicateProductError(InventoryError):
    pass

class InvalidProductDataError(InventoryError):
    pass


# Abstract Base Class
class Product(abc.ABC):
    def __init__(self, product_id: str, name: str, price: float, quantity_in_stock: int):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Price must be positive")
        self._price = new_price

    @property
    def quantity_in_stock(self) -> int:
        return self._quantity_in_stock

    def restock(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Restock amount must be positive")
        self._quantity_in_stock += amount

    def sell(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Sale quantity must be positive")
        if quantity > self._quantity_in_stock:
            raise InsufficientStockError(
                f"Not enough stock. Available: {self._quantity_in_stock}, Requested: {quantity}"
            )
        self._quantity_in_stock -= quantity

    def get_total_value(self) -> float:
        return self._price * self._quantity_in_stock

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def to_dict(self) -> Dict:
        pass

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, data: Dict) -> 'Product':
        pass


# Product Subclasses
class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._warranty_years = warranty_years
        self._brand = brand

    @property
    def warranty_years(self) -> int:
        return self._warranty_years

    @property
    def brand(self) -> str:
        return self._brand

    def __str__(self) -> str:
        return (f"Electronics - ID: {self._product_id}, Name: {self._name}, "
                f"Brand: {self._brand}, Price: ${self._price:.2f}, "
                f"Warranty: {self._warranty_years} years, Stock: {self._quantity_in_stock}")

    def to_dict(self) -> Dict:
        return {
            'type': 'electronics',
            'product_id': self._product_id,
            'name': self._name,
            'price': self._price,
            'quantity_in_stock': self._quantity_in_stock,
            'warranty_years': self._warranty_years,
            'brand': self._brand
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Electronics':
        return cls(data['product_id'], data['name'], data['price'],
                   data['quantity_in_stock'], data['warranty_years'], data['brand'])


class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()

    @property
    def expiry_date(self) -> date:
        return self._expiry_date

    def is_expired(self) -> bool:
        return self._expiry_date < date.today()

    def __str__(self) -> str:
        expired = " (EXPIRED)" if self.is_expired() else ""
        return (f"Grocery - ID: {self._product_id}, Name: {self._name}, "
                f"Price: ${self._price:.2f}, Expiry: {self._expiry_date}{expired}, "
                f"Stock: {self._quantity_in_stock}")

    def to_dict(self) -> Dict:
        return {
            'type': 'grocery',
            'product_id': self._product_id,
            'name': self._name,
            'price': self._price,
            'quantity_in_stock': self._quantity_in_stock,
            'expiry_date': self._expiry_date.strftime("%Y-%m-%d")
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Grocery':
        return cls(data['product_id'], data['name'], data['price'],
                   data['quantity_in_stock'], data['expiry_date'])


class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._size = size
        self._material = material

    @property
    def size(self) -> str:
        return self._size

    @property
    def material(self) -> str:
        return self._material

    def __str__(self) -> str:
        return (f"Clothing - ID: {self._product_id}, Name: {self._name}, "
                f"Size: {self._size}, Material: {self._material}, "
                f"Price: ${self._price:.2f}, Stock: {self._quantity_in_stock}")

    def to_dict(self) -> Dict:
        return {
            'type': 'clothing',
            'product_id': self._product_id,
            'name': self._name,
            'price': self._price,
            'quantity_in_stock': self._quantity_in_stock,
            'size': self._size,
            'material': self._material
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Clothing':
        return cls(data['product_id'], data['name'], data['price'],
                   data['quantity_in_stock'], data['size'], data['material'])
