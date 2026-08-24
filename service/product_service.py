from logs.logger import log_event
from dao.products_dao import ProductDAO
from dao.categories_dao import CategoryDAO

class ProductService:
    def __init__(self):
        self.product_dao = ProductDAO()
        self.category_dao = CategoryDAO()

    def add_product(self, product):
        if not product.product_name.strip():
            log_event("Validation failed: " + str("Product name cannot be empty"))
            raise ValueError("Product name cannot be empty")
        if product.unit_price <= 0:
            log_event("Validation failed: " + str("Unit price must be greater than 0"))
            raise ValueError("Unit price must be greater than 0")
        log_event("Service operation successful")
        return self.product_dao.add_product(product)

    def get_all_products(self):
        log_event("Service operation successful")
        return self.product_dao.get_all_products()

    def get_product_by_id(self, product_id):
        if product_id <= 0:
            log_event("Validation failed: " + str("Invalid product ID"))
            raise ValueError("Invalid product ID")
        log_event("Service operation successful")
        return self.product_dao.get_product_by_id(product_id)

    def update_product(self, product):
        if not product.product_name.strip():
            log_event("Validation failed: " + str("Product name cannot be empty"))
            raise ValueError("Product name cannot be empty")
        if product.unit_price <= 0:
            log_event("Validation failed: " + str("Unit price must be greater than 0"))
            raise ValueError("Unit price must be greater than 0")
        log_event("Service operation successful")
        return self.product_dao.update_product(product)

    def delete_product(self, product_id):
        if product_id <= 0:
            log_event("Validation failed: " + str("Invalid product ID"))
            raise ValueError("Invalid product ID")
        log_event("Service operation successful")
        return self.product_dao.delete_product(product_id)

    def add_category(self, category):
        if not category.category_name.strip():
            log_event("Validation failed: " + str("Category name cannot be empty"))
            raise ValueError("Category name cannot be empty")
        log_event("Service operation successful")
        return self.category_dao.add_category(category)
