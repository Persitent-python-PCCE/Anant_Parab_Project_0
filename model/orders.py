class Orders:
    def __init__(self, user_id, discount=0, total_amount=0, status="Pending", order_date=None, order_id=None):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.discount = discount
        self.total_amount = total_amount
        self.status = status