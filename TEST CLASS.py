
from faker import Faker

print(dir(Faker()))
f =Faker().image()
print(type(f), f)