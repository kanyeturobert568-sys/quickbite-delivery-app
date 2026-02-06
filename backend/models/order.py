class Order:
    def __init__(self, order_id, status, customer):
        self.order_id = order_id
        self.status = status
        self.customer = customer

    def update_status(self, new_status):
        self.status = new_status

    def __repr__(self):
        return f"Order(order_id={self.order_id}, status={self.status}, customer={self.customer})"