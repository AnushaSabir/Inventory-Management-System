# inventory.py

import json
from typing import Dict, List, Type
from product import Product, Electronics, Grocery, Clothing, DuplicateProductError, InvalidProductDataError


class Inventory:
    def __init__(self):
        self._products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        if product.product_id in self._products:
            raise DuplicateProductError(f"Product ID {product.product_id} already exists")
        self._products[product.product_id] = product

    def remove_product(self, product_id: str) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID {product_id} not found")
        del self._products[product_id]

    def search_by_name(self, name: str) -> List[Product]:
        return [p for p in self._products.values() if name.lower() in p.name.lower()]

    def search_by_type(self, product_type: Type[Product]) -> List[Product]:
        return [p for p in self._products.values() if isinstance(p, product_type)]

    def list_all_products(self) -> List[Product]:
        return list(self._products.values())

    def sell_product(self, product_id: str, quantity: int) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID {product_id} not found")
        self._products[product_id].sell(quantity)

    def restock_product(self, product_id: str, quantity: int) -> None:
        if product_id not in self._products:
            raise KeyError(f"Product ID {product_id} not found")
        self._products[product_id].restock(quantity)

    def total_inventory_value(self) -> float:
        return sum(p.get_total_value() for p in self._products.values())

    def remove_expired_products(self) -> List[Product]:
        expired = []
        for product_id, product in list(self._products.items()):
            if isinstance(product, Grocery) and product.is_expired():
                expired.append(self._products.pop(product_id))
        return expired

    def save_to_file(self, filename: str) -> None:
        data = {'products': [product.to_dict() for product in self._products.values()]}
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        with open(filename, 'r') as f:
            data = json.load(f)

        self._products = {}
        product_classes = {
            'electronics': Electronics,
            'grocery': Grocery,
            'clothing': Clothing
        }

        for product_data in data['products']:
            try:
                product_type = product_data['type']
                if product_type not in product_classes:
                    raise InvalidProductDataError(f"Unknown product type: {product_type}")
                product = product_classes[product_type].from_dict(product_data)
                self.add_product(product)
            except KeyError as e:
                raise InvalidProductDataError(f"Missing required field: {e}")
