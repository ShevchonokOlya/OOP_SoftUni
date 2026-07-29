from project import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product:Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        return next((prod for prod in self.products if prod.name == product_name), None)

    def remove(self, product_name: str) -> None:
        target_product = self.find(product_name)
        self.products.remove(target_product) if target_product else None


    def __repr__(self) -> str:
        result = ''
        for pr in self.products:
            result += f'{pr.name}: {pr.quantity}\n'
        return result.strip()

