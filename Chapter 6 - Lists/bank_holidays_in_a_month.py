bank_holidays_in_a_month=[1,0,1,1,2,0,0,1,0,0,0,2]

def bank_holiday(month):
    return bank_holidays_in_a_month[month-1]

month = int(input('Enter the month as a number: '))
amount = bank_holiday(month)
print(f'There are {amount} bank holidays in month {month}')
