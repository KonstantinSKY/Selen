# def sum_list(l):
#     sum = 0
#
#
#
#     for x in l:
#         sum = sum + x
#
#         print(sum)
#     return sum
#
#
# l = [1, 2, 3, 4, 5]
# print(sum_list(l))
# #
#
#
#
# number = 325
# while number > 100:
#     number = number - 1
#
#
#     print(number)

import faker
from datetime import  datetime

fake = faker.Faker()

# print(type(fake.first_name()))
# print(fake.month_name()+" "+fake.year())
#
# print(type(datetime.now()))

num = fake.date().split("-")
print(type(num))
num.reverse()
print(num)
num_reverse = ("/").join(num)
print(num_reverse)
num1 = fake.time()[:-3]
print(num_reverse,  num1)