#exercise 1
def fizzbuzz(n):
    if n % 3 ==0:
        print('Fizz')
    elif n%5==0:
        print('Buzz')
    elif n%3==0 & n%5==0:
        print('FizzBuzz')
    else:
        print(n)

fizzbuzz(1)
fizzbuzz(20)

#exercise 2
mix_data=[3,4.7,'12',59,0.8,'monica',1001]
only_integer=list(item for item in mix_data if isinstance(item,int))
print(only_integer)

#exercise 3
todo_list=[]
def add_task(task):
    todo_list.append(task)

def show_tasks():
    print(todo_list)

#exercise 4
def celsius_to_fahrenheit(celsius):
    print((celsius*9/5)+32)

celsius_to_fahrenheit(22)
celsius_to_fahrenheit(46)
celsius_to_fahrenheit(51)
celsius_to_fahrenheit(76)



