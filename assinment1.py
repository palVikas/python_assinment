#! python3
#shebang line
#print the add of the given number

number = (input("enter the number : "))




def sum_of_digit(num):
    length = len(number)
    sum = 0
  
    for ren in range(int(length)):
        last_digit = int(num)%10
        num = int(int(num)/10)
        sum += last_digit
       
    return sum 
     


print("sum of the digit is: "+str(sum_of_digit(number)))



x = list(range(1,11))

print(x)
    
    
