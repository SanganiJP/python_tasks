def most_common_complaint(complaints):
    high = 0
    name = ''
    for key,val in complaints.items():
        if high<val:
            name=''
            high=val
            name += key
    return name

def total_complaint(complaints):
    total_complaint = 0
    for val in complaints.values():
        total_complaint += val
    return total_complaint

def complaint_percentage(complaints):
    cp={}
    for key,val in complaints.items():
        cp[key] = f'{(val/total_complaint(complaints))*100}%'
    return cp

complaints = {
    "Late Delivery": 120,
    "Damaged Product": 95,
    "Wrong Item": 60,
    "Customer Service": 75,
    "Billing Issues": 50
}

print(f'Most common complaints : {most_common_complaint(complaints)}')
print(f'Complaint Percentage Distribution : {complaint_percentage(complaints)}')

