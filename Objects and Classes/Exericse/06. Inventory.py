class Inventory:

    def __init__(self, __capacity: int):
        self.__capacity = __capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        left_capacity = self.__capacity - len(self.items)
        items_final = ", ".join(self.items)
        return f"Items: {items_final}.\nCapacity left: {left_capacity}"
