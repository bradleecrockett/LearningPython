import random
print("*******Rounding******")

x = 0.0037 / 100
# These numbers look equal!
y = 0.000037
# But they aren't exactly equal!
print(x)
print(y)
if (x == y):
    print("Equal!")
else:
    print("Unequal!")

# ... But they are approximately equal
# (to five decimal places)!
if round(x, 5) == round(y, 5):
    print("Approximately equal!")
else:
    print("Not approximately equal!")


print("******Break**********")

# This for loop only prints 0 through 4.
for i in range(10):
    if i == 5:
        break
    print(i)


print("******Continue*********")

# we skip back to the top of the for loop
for i in range(10):
    if i == 5:
        continue
    print(i)


print("*******While*********")

x = 0
while (x < 10):
    print(x)
    x = x + 1


print("after the loop x is: ", x)


print("*****Loop and a half****")

magic_number = 7
while (True):
    guess = int(input("Guess my number: "))
    if guess == magic_number:
        print("You got it!")
        break
    # Next line is NOT reached if the condition
    print("Try again!")


print("*****Using Exceptions***")

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


# print("******What is the output 1******")
#
# size = 5
# for a in range(size):
#     for b in range(size):
#         print(a, b)
#
#
# # print("******What is the output 2*****")
# #
# # total = 0
# # for c in range(5):
# #     d = 1
# #     while d <= c:
# #         total = total + d
# #         d += 1
# #
# # print(total)
# #
# #
# # print("*****What is the output 3******")
# #
# # # power2 = 1
# # # while(power2 != 20):
# # #     print(power2)
# # #     power2 *= 2