squares =  [value**2 for value in range(1,11)]
print(squares)

numbers_1 = list(range(1,1000001))
print(min(numbers_1))
print(max(numbers_1))
print(sum(numbers_1))

numbers_2 = list(range(1,20,2))
for number_2 in numbers_2:
    print(number_2)  # 1,3,5,7,9,11,13,15,17,19

numbers_3 = list(range(3,31,3))
for number_3 in numbers_3:
    print(number_3)  # 3,6,9,12,15,18,21,24,27,30   

numbers_4 = [value ** 3 for value in range(1,11)]
print(numbers_4)  # 1,8,27,64,125,216,343,512,729,1000