from functools import reduce

def total_sale_of_product(sales_data):
    total_sale = {}
    for store in sales_data.values():
        for product, count in store.items():
            # print(f'{product}:{count}')
            if total_sale.get(product):
                total_sale[product] += count
            else:
                total_sale[product] = count

    #print(total_sale)
    return total_sale

def total_sale_of_store(sales_data):
    sale_of_store = {}
    for store, sale in sales_data.items():
        total = 0
        for val in sale.values():
           total += val
        sale_of_store[store] = total
    return sale_of_store

def best_selling_product(total_sale_of_stores):
    max_sale = 0
    name = ""
    for key, val in total_sale_of_stores.items():
        if val > max_sale:
            name = ""
            max_sale = val
            name += key
    return name,max_sale
    # print(f"{name}:{max_sale}")

def best_selling_store(total_sale_of_products):
    high_sale_p = 0
    p_name = ""
    for key, val in total_sale_of_products.items():
        if val > high_sale_p:
            p_name = ""
            high_sale_p = val
            p_name += key
    return p_name, high_sale_p
    # print(f"{p_name}:{high_sale_p}")


def sorted_sales_data(total_sale_of_stores):
    stores = sorted(total_sale_of_stores.items(), key=lambda s: s[1], reverse=True)
    print(f'1.{stores[0][0]}:{stores[0][1]}')
    print(f'2.{stores[1][0]}:{stores[1][1]}')
    print(f'3.{stores[2][0]}:{stores[2][1]}')

sales_data = {
    "Store_A": {
        "Laptop": 15,
        "Phone": 30,
        "Tablet": 10
    },
    "Store_B": {
        "Laptop": 25,
        "Phone": 20,
        "Tablet": 15
    },
    "Store_C": {
        "Laptop": 10,
        "Phone": 35,
        "Tablet": 5
    }
}

total_sale_of_products = total_sale_of_product(sales_data)
print(total_sale_of_products)

total_sale_of_stores = total_sale_of_store(sales_data)
print(total_sale_of_stores)

name,max_sales =best_selling_product(total_sale_of_stores)
print(f'{name}:{max_sales}')

p_name,high_sale_p = best_selling_store(total_sale_of_products)
print(f'{p_name}:{high_sale_p}')

sorted_sales_data(total_sale_of_stores)

# stores = sorted(total_sale_of_stores.items(), key= lambda s:s[1], reverse=True)

# print(highestselling_product)

