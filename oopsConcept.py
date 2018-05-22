# webbrowser
import webbrowser

class Mobile():
    def __init__(self , brand_name , model_name , price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def serch_online(self):
        webbrowser.open(self.model_name)



motoX = Mobile("Motorola" , "Moto x 500" , 67000)

def sum(a,b):
    return a+b

print(sum(4,8))

sum1 = lambda a,b: a+b
print(sum1(9,8))

#list comprehension
#create a list from 1 to 20

number = []
for i in range(1,21):
    number.append(i)

print(number)

number = [x for x in range(1,11)]

print(number)

squre = [x**2 for x in range(1,11)]

print(squre)

times2 =  [i*2 for i in squre]
print(times2)


#divisible by 3 or 5
print('divisible by 3 or 5')
number = [i for i in range(1,101) if i%3 ==0 and i%5 ==0]
print(number)

#print even number in range
print('even number between 1 to 100')

number = [x for x in range(1,101) if x%2==0]
print(number)

