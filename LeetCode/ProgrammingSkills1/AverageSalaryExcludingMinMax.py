# You are given an array of unique integers salary where 
# salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding
#  the minimum and maximum salary.
def average(salary):
    min = salary[0]
    max = salary[0]
    sum=0
    for i in salary:
        if min > i:
            min = i 
        if max < i:
            max = i
        sum+=i 
    return (sum-min-max)/(len(salary)-2)

print(average(list(map(int,input("Enter array of salary to find average salary excluding min and max salary.\n").split()))))
