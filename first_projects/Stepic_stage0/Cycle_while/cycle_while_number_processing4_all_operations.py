num = int(input())
total = 0
amount = 0
multiply = 1
average = 0
first_num = 0
sum_first_and_last = 0
num1 = num
while num != 0:
    last_digit = num % 10
    total += last_digit
    amount += 1
    multiply *= last_digit
    num = num // 10
average = total / amount
first_num = num1 // 10 ** (amount - 1)
last_num = num1 % 10
sum_first_and_last = first_num + last_num
print(total)
print(amount)
print(multiply)
print(average)
print(first_num)
print(sum_first_and_last)