def find_high_performer(marketing_performance):
    performanse = 0
    chennle=''
    for key,val in marketing_performance.items():
        if performanse < val:
            chennle=''
            performanse = val
            chennle += key
    return f'{chennle}({performanse}%)'

def average_conversion_rate(marketing_performance):
    avg=0
    chennle = 0
    for val in marketing_performance.values():
        avg += val
        chennle +=1
    return f'{avg/chennle}%'

marketing_performance = {
    "Facebook Ads": 3.2,
    "Google Ads": 4.8,
    "Email Marketing": 2.5,
    "Organic Search": 5.6,
    "Referral": 3.9
}

print(f'High performer : {find_high_performer(marketing_performance)}')
print(f'Average Conversion Rate : {average_conversion_rate(marketing_performance)}')