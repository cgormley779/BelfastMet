print(f'Hello I am TechComps System Monitoring AI')
cpu = int(input(f'Please enter current CPU usage from 0-100% '))
#This line prompts the user to input CPU usage in perecentage
memory = float(input(f'Please enter your current memory usage in GB '))
#this line prompts the user to input memory use in percentage and store it in a variable

def cpu_usage(cpu):
    if cpu < 40:
        return str(f'Underutilized')
    elif cpu < 75:
        return str(f'Optimal')
    elif cpu > 75:
        return str(f'Overloaded')
    else:
        print (f'This is not a valid answer')
#this creates a function which returns a string based on if user input falls into a range e.g. if cpu usage is
#less than 40% then the result will be "underutilized"

def memory_usage(memory):
    if memory < 4:
        return str(f'Underutilized')
    elif memory < 8:
        return str(f'Optimal')
    elif memory > 8:
        return str(f'Overloaded')
    else:
        print (f'This is not a valid answer')
#This function mirrors the cpu_usage function

memory_function = memory_usage(memory)
#this stores the result of memory_usage function as a variable to be called for later use
cpu_function = cpu_usage(cpu)
#this stores the result of cpu_function as a variable to be called for later use

print(f'Your cpu usage is {cpu_function} and your memory usage is {memory_function}')
#this line prints the results of the 2 function using the users input and the associated utilization






    