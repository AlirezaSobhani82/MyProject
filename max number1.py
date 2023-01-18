number = range(1,11)
max = 0
for each_number in number:
    num = int(input("please insert the number{}:".format(each_number)))
    if num > max:
        max = num

print("the maximum number is {}".format(max))