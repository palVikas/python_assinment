#write a programme using function to sum of given number using user
first_number = int(input("enter the first number: "))
second_number = int(input("enter the second number: "))

def add_number(a,b):
    return a+b


sum = add_number(first_number,second_number);
print (sum)

#write a programe to prite a series a given number
number = int(input("enter a number: "))
for num in range(1,number+1):
    print(num)


#factorial of a given number

number = int(input("enter a number you want to factorial: "))

def factorial(num):
    if (num==1 or num ==0):
        return 1
    return num*factorial(num-1)

print (factorial(number))


#write a programe to print ap series of given number

first_term = int(input("enter the first term of the AP series: "))

difference = int(input("enter the difference of the AP Series: "))

number_of_terms = int(input("enter the number of terms of the AP Series: "))
series = ""+str(first_term)


for num_of_trm in range(1,number_of_terms):
    
    series += ","+str(first_term+difference)
    first_term = (first_term+difference)

print(series)


    
    


