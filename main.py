from PurchaseTracker import PurchaseTracker

purchase_tracker = PurchaseTracker()
purchase_tracker.load_report()
purchase_tracker.add_product_data()
purchase_tracker.show_report()
purchase_tracker.write_report()