# session 1

#exercise 1
greeting='Hello world!'
print(greeting)

#exercise 2
a=3
b=7
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#exercise 3
name='Monica'
print(f'Hello {name}!')

#exercise 4
universities=['ESADE','RSM','ESSEC','IE','Bocconi']
print(universities)
print(universities[0])
print(universities[-1])

#exercise 5
student={'name':'Monica','age':20,'grade':9}
for key in student:
    print(f'{key}:{student[key]}')

#exercise 6
coordinates=(14,60)
print(coordinates[0])
print(coordinates[1])

#exercise 7
colors={'red','green','blue'}
colors.add('pink')
colors.add('green')
print(colors)
colors.discard('red')
light_colors={'light blue','pastel green','lilac','butter yellow','pink'}
merged_colors=colors|light_colors
print(merged_colors)

#exercise 8
num=8
if num>0:
    print(f'{num} is positive')
elif num<0:
    print(f'{num} is negative')
elif num==0:
    print(f'{num} is zero')

#exercise 9
list_numbers=[number for number in range(1,6)]
for n in list_numbers:
    print(n)

#exercise 10
i=1
while i<6:
    print(i)
    i+=1

#exercise 11
grade=input('Input a grade: ').upper()
match grade:
    case 'A':
        print('Excellent!')
    case 'B':
        print('Good job!')
    case 'C':
        print('Fair')
    case 'D':
        print('Needs improvement')
    case 'F':
        print('Failing')
    case _:
        print('You did not enter a grade, please retry')

#exercise 12
def greet(name):
    print(f'Hello, {name}!')
greet('Monica')

#exercise 13
def square(number):
    return number**2

print(square(3))
print(square(7))
print(square(9))


#exercise 14
def multiply(a,b=1):
    return a*b 

print(multiply(3,2))
print(multiply(3))

#exercise 15
num_list=[l for l in range(1,11)]
new_list=[]
for item in num_list:
    new_list.append(item**2)
print(new_list)

#exercise 16
student_grades={'Azriel':[9,7.5,8,8.7],
                'Feyre':[6,6.4,7,9.2],
                'Rhysand':[9.8,8.1,9.3,10]}
for student in student_grades:
    average=sum(student_grades[student])/len(student_grades[student])
    print(f'{student} average grade is {average}')

#exercise 17
def calculate(num1,num2,operator):
    if operator== '+':
        return num1 + num2
    elif operator== '-':
        return num1 - num2
    elif operator== '*':
        return num1 * num2
    elif operator== '/':
        return num1 / num2
    else:
        print('invalid operator, please retry with +,-,* or /')
first=float(input('please input the first number: '))
second=float(input('please input the second number: '))
op=input('please input what operator would you like to use: ')

calculate(first,second,op)