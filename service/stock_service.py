from dao.stock_dao import StockDAO

class StockService:
    def __init__(self):
        self.stock_dao = StockDAO()

    def add_or_update_stock(self, product_id, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.stock_dao.add_or_update_stock(product_id, quantity)

    def get_stock(self, product_id):
        return self.stock_dao.get_stock_by_product(product_id)
