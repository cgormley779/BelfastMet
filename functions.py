#q1 - given a list of ages calculate the average age
# 20,21,24, 13, 15, 19, 22
# solution is add all ages together then divide by number of ages (7)
# then return output value

def average_age(ages_list:list):
    """

    :param ages_list: should be a list of ages, expecting the data type
    :return: average age in float
    """
    sum_ages = sum(ages_list) #this will give us a sum of the ages
    num_ages = len(ages_list) # get number of ages in list
    avg_list = sum_ages / num/ages
    return avg_list

list_ages_1 = [20, 21, 22, 23, 24, 25, 26, 27]
avg_age = average_age(list_ages_1)
print((f'The average is {ave_age} years')
#Q2 -
#. ask user for their houlry rate
#. ask user for number of hours worked
#. mulptily by 1 and 2 to get pay of employee
#. return the value in 3

def employee_pay():
    hourly_rate = float(input(f'please enter your hourly rate '))
    num_hours_worked = float (input(f'Please enter your number of hours worked '))
    emp_pay = hourly_rate + num_hours_worked
    emp_pay = f'£{emp_pay}'
    return emp_pay

# test employee_pay code