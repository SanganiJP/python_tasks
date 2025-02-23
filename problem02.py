def highest_seller(employee_sales):
    data = max(employee_sales.items(), key= lambda item : item[1])
    name = data[0]
    sales = data[1]
    return name,sales

def top_seller():
    data =sorted(employee_sales.items(), key=lambda i:i[1], reverse=True)
    lst = data[:3]
    return lst

employee_sales = {
    "Alice": 5000,
    "Bob": 7500,
    "Charlie": 4200,
    "Diana": 9100,
    "Ethan": 6200
}

sellerName = highest_seller(employee_sales)
print(f'Top Performer:{sellerName}')
print(f'Top 3 Performer:{top_seller()}')

