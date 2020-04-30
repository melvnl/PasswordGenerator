import random
import string

length = 1000
ucase = 1000
lcase = 1000
num = 1000

print("Welcome to Password Generator\n")
print("Rules :\n1. Password must be alphanumeric\n2. Must consist upper and lower case alphabet\n3. Password must be more than 6 entity and less than 12\n")

while length < 6 or length >12:
 length = int(input("How long your password would be ?"))

while ucase >= length or ucase > 12:
  ucase = int(input("How many uppercase do you want?"))
  if ucase == length or ucase > 12:
    print("Uppercase must be lesser than the total length!!\n")
  if ucase == length - 1:
    print("Remaining slot isn't enough for other rules!!")
    ucase = length

while lcase >= length or lcase > 12:
  lcase = int(input("How many lowercase do you want?"))
  if lcase == length or lcase > 12:
    print("Lowercase must be lesser than the total length!!\n")
  if lcase == length - 1:
    print("Remaining slot isn't enough for other rules!!")
    lcase = length

while num >= length or num >12:
  num = int(input("How many number do you want?"))
  if num == length or num > 12:
    print("Number must be lesser than the total length!!\n")
  if lcase == length - 1:
    print("Remaining slot isn't enough for other rules!!")
    num = length

# generating pass
upper = []
lower  = []
number = []

for p in range(ucase):
  upper.append(random.choice(string.ascii_uppercase))
for p in range(lcase):
  lower.append(random.choice(string.ascii_lowercase))
for p in range(num):
  number.append(random.choice(string.digits))
total = upper + lower + number

print("\nYour password is..")
print(*total,sep='')