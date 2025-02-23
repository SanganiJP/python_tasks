def highest_revenue(revenue_per_store):
    max_r=0
    sn = ""
    for key,val in revenue_per_store.items():
        if val>max_r:
            sn=""
            max_r=val
            sn += key
    return sn

def find_revenue_per_store(sales_data):
    revenue_per_store = {}
    for store, products in sales_data.items():
        total_revenue = 0
        for product, quantity in products.items():
            total_revenue += quantity * product_prices[product]
        revenue_per_store[store] = total_revenue
    return revenue_per_store

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

print(f'Revenue Per Store : {find_revenue_per_store(sales_data)}')
store_name = highest_revenue(revenue_per_store=find_revenue_per_store(sales_data))
print(f'Most profitable store: {store_name}')