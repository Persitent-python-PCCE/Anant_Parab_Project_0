from logs.logger import log_event
from service.product_service import ProductService
from service.stock_service import StockService
from model.products import Products
from model.categories import Categories

class ProductController:
    def __init__(self):
        self.product_service = ProductService()
        self.stock_service = StockService()

    def add_product(self):
        try:
            print("\n--- Add Product ---")
            name = input("Enter product name: ")
            cat_id = int(input("Enter category ID: "))
            price = float(input("Enter unit price: "))
        
            product = Products(product_name=name, category_id=cat_id, unit_price=price)
            p_id = self.product_service.add_product(product)
            print("Product added successfully, ID:", p_id)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in add_product: {e}")

    def update_product(self):
        try:
            print("\n--- Update Product ---")
            p_id = int(input("Enter product ID to update: "))
            name = input("Enter new product name: ")
            cat_id = int(input("Enter new category ID: "))
            price = float(input("Enter new unit price: "))
        
            product = Products(product_name=name, category_id=cat_id, unit_price=price, product_id=p_id)
            affected = self.product_service.update_product(product)
            if affected:
                print("Product updated successfully")
            else:
                print("Product not found")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in update_product: {e}")

    def delete_product(self):
        try:
            print("\n--- Delete Product ---")
            p_id = int(input("Enter product ID to delete: "))
            affected = self.product_service.delete_product(p_id)
            if affected:
                print("Product deleted successfully")
            else:
                print("Product not found")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in delete_product: {e}")

    def view_all_products(self):
        try:
            print("\n--- All Products ---")
            products = self.product_service.get_all_products()
            for p in products:
                print(f"ID: {p['product_id']} | Name: {p['product_name']} | Price: {p['unit_price']} | Cat: {p['category_id']}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in view_all_products: {e}")

    def add_category(self):
        try:
            print("\n--- Add Category ---")
            name = input("Enter category name: ")
            cat = Categories(category_name=name)
            c_id = self.product_service.add_category(cat)
            print("Category added successfully, ID:", c_id)

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in add_category: {e}")

    def manage_stock(self):
        try:
            print("\n--- Manage Stock ---")
            p_id = int(input("Enter product ID: "))
            quantity = int(input("Enter quantity to add (positive): "))
            self.stock_service.add_or_update_stock(p_id, quantity)
            print("Stock updated successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            log_event(f"Controller ERROR in manage_stock: {e}")

