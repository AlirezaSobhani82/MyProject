#maximum

def max_number(num1 , num2 , num3):
    if num1 > num2 and num1 > num3:
        max = num1
    elif num2 > num1 and num2 > num3:
        max = num2
    else:
        max = num3

    print("max number betwen %d , %d and %d is: %d" %(num1 , num2 , num3 , max))


number1 = int(input("please insert the number1: "))
number2 = int(input("please insert the number2: "))
number3 = int(input("please insert the number3: "))

max_number(number1 , number2 , number3)