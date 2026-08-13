class Products:
    def __init__(self, product_name, category_id, unit_price, product_id=None):
        self.product_id = product_id
        self.product_name = product_name
        self.category_id = category_id
        self.unit_price = unit_price