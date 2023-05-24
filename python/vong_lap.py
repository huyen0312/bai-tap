# hàm range([start],stop,[step])

for number in range(3,12):
    print(number)

for char in 'Nguyen Huyen':
    print(char)

number = 0
while number < 12:
    number += 1
    print(number)

numbers = range(1,100,30)
for i in numbers:
    if i <60 :
        continue
    print(i)

for i in numbers:
    if i >=70:
        break
    print(i)


def helloPython(): # hàm tự định nghĩa
    print('Hello, Python!')
helloPython()

language =('Python')
print('Hello, %s!' %(language))

def hello (language):
    print('Nguyen %s' %(language))
hello('Huyen')

number_1 = 3
number_2 = 12
def sum (a, b):
    return a + b
total = sum(number_1, number_2)
print('Tổng của %s và %s là %s' %(number_1,number_2,total))

def hello():
    print('hello!')
    return
    print('xin chào')
hello()