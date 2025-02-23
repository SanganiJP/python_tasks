def highest_revenue(revenue_per_store):
    return max(revenue_per_store.items(), key= lambda i : i[1])[0]

def find_revenue_per_store(sales_data):
    revenue_per_stores = {}
    for store, products in sales_data.items():
        total_revenue = 0
        for product, quantity in products.items():
            total_revenue += quantity * product_prices[product]
        revenue_per_stores[store] = total_revenue
    return revenue_per_stores

sales_data = {
    "Store_A": {"Laptop": 15, "Phone": 30, "Tablet": 10},
    "Store_B": {"Laptop": 25, "Phone": 20, "Tablet": 15},
    "Store_C": {"Laptop": 10, "Phone": 35, "Tablet": 5}
}

product_prices = {
    "Laptop": 1000,
    "Phone": 500,
    "Tablet": 300
}

revenue_per_store=find_revenue_per_store(sales_data)
print(f'Revenue Per Store : {revenue_per_store}')
store_name = highest_revenue(revenue_per_store)
print(f'Most profitable store: {store_name}')