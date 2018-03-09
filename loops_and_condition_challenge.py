'''This program Create a new list of strings called thousand_or_greater that only contains the names shared by 1,000 people or more.

To accomplish this:

Create an empty list and assign it to thousand_or_greater.
Write a for loop that iterates over numerical_list.
In the loop body, use an if statement to determine if the value at index 1 for that element (which is a list) is greater than or equal to 1000.
If the value is greater than or equal to 1000, use the append() method to add its name to thousand_or_greater.
Finally, display the first 10 elements in thousand_or_greater.
'''
# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater=[]
for i in numerical_list:
    if i[1]>1000:
        thousand_or_greater.append(i[0])
print(thousand_or_greater[0:5])
