def find_high_performer(marketing_performance):
    data=max(marketing_performance.items(), key= lambda i:i[1])
    chennle = data[0]
    performanse = data[1]
    return f'{chennle}({performanse}%)'

def average_conversion_rate(marketing_performance):
    avg = sum(marketing_performance.values())/len(marketing_performance)
    return f'{avg}%'

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

print(f'High performer : {find_high_performer(marketing_performance)}')
print(f'Average Conversion Rate : {average_conversion_rate(marketing_performance)}')