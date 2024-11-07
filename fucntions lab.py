# write a function that returns the largest of 2 user entered numbers
# use input function for number 1 and numbr 2
# use return with an if statement to return the largest number
# print return value

#second part = use lambda to do the same and compare numbers

# Q1:
def compare_number (x,y):
    if y>x:
        return y
    elif x > y:
        return x
    else: return None

x = input(f'input number ')
y = input(f'input number ')
result = compare_number(x,y)
print(f'The greatest number is {result}')


second_answer = lambda x, y : max(x,y)
