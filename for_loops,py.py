'''
This program creates a list of integers named int_crime_rates that contains just the crime rates - as integers - from the list rows.

First create an empty list and assign it to a new variable int_crime_rates.
Then, write a for loop that iterates over rows and does the following:
uses the split() method to convert each string in rows into a list, based on the comma delimiter
converts the value at index 1 from that list to an integer using the int() function
uses the append() method to add each integer to int_crime_rates
'''

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates=[]
for ele in rows:
    elem=ele.split(',')
    eleme=int(elem[1])
    int_crime_rates.append(eleme)
