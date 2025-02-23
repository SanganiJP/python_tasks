def most_common_complaint(complaints):
    return max(complaints.items(),key=lambda item:item[1])[0]

def complaint_percentage(complaints):
    cp={}
    for key,val in complaints.items():
        cp[key] = f'{(val/sum(complaints.values()))*100}%'
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

