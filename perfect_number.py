def is_perfect_number(number):
    if number <2:
        return False
    divisor_sum= sum(i for i in range(1,number) if number %i == 0)
    return divisor_sum==number

print("1 ile 1000 arasındaki mükemmel sayılar : ")
for num in range(1,1001):
    if is_perfect_number(num):
        print(num)