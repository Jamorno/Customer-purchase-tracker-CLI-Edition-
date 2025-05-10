import json

class PurchaseTracker:
    def __init__(self):
        self.purchase = {}

    def add_product_data(self):
        while True:
            customer_name = input("Enter customer name(type end to exit): ")
            if customer_name == "end":
                break
            product_name = input("Enter product name: ")
            price = int(input("Enter product price: "))

            if customer_name not in self.purchase:
                self.purchase[customer_name] = {}
            self.purchase[customer_name][product_name] = price
            print(f"Added - {customer_name}: {product_name}({price})")

    def show_report(self):
        total = 0
        for name, product in self.purchase.items():
            print(f"{name}:")
            person_total = 0
            for products, count in product.items():
                print(f"- {products}: {count}")

                person_total += count
            print(f"Total({name}) = {person_total}")

            total += person_total
        print(f"Total = {total}")

    def write_report(self):
        with open("customer_purchase_tracker.json", "w") as file:
            json.dump(self.purchase, file)

        print("Write report complete")

    def load_report(self):
        try:
            with open("customer_purchase_tracker.json", "r") as file:
                self.purchase = json.load(file)
        except FileNotFoundError:
            self.purchase = {}
