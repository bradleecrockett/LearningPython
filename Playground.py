import random

# we skip back to the top of the for loop
for i in range(10):
    if i == 5:
        continue
    print(i)

print("***********************")

size = 5
for a in range(size):
    for b in range(size):
        print(a, b)


print("***********************")

x = 0
while (x < 10):
    print(x)
    x = x + 1

print("after the loop x is: ", x)

print("***********************")

magic_number = 7
while (True):
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("You got it!")
        break
    # Next line is NOT reached if the condition
    print("Try again!")

print("***********************")

while(True):
    try:
        num = int(input("Enter a positive number: "))
        if(num<0):
            continue
        else:
            break
    except ValueError:
        print("That was not a number.")

print("The positive number is: ", num)

# print("***********************")
#
# total = 0
# for c in range(5):
#     d = 1
#     while d <= c:
#         total = total + d
#         d += 1
#
# print(total)
#
# print("***********************")
#
# # power2 = 1
# # while(power2 != 20):
# #     print(power2)
# #     power2 *= 2