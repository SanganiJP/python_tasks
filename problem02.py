def highest_seller(employee_sales):
    high=0
    name=''
    for key,val in employee_sales.items():
        if high<val:
            name=''
            high = val
            name += key
    return name,high

def top_seller():
    lst = []
    for emp in range(3):
        sellerName, high = highest_seller(employee_sales)
        lst.append(highest_seller(employee_sales))
        employee_sales.pop(sellerName)
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
print(top_seller())


# lst.append(highest_seller(employee_sales))
# sellerName,high = highest_seller(employee_sales)
# employee_sales.pop(sellerName)
#
# lst.append(highest_seller(employee_sales))
# sellerName,high = highest_seller(employee_sales)
# employee_sales.pop(sellerName)
