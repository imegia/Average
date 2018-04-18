#Import the built in Python 3.4 module
import statistics

#Make a list 
a = [2, 5, 6, 6]

#Median - finds the middle value
#Method - order them from smallest to biggest and find the middle number
print(statistics.median(a))

#Mode - finds most common value
#Method - order them from smallest to biggest and find the most common value
print(statistics.mode(a))


#Mean - finds the average
#Method - sum all numbers in list and divide by the number of values in the list
print(statistics.mean(a))
