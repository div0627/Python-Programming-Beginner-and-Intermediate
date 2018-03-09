'''This program finds the largest integer in crime_rates using the strategy we just outlined, and assign that value to the variable highest.
'''

print(crime_rates)
highest=crime_rates[0]
for i in crime_rates:
    if i>highest:
        highest=i
