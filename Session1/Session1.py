#----------------------------------------------------------------
# SESSION 1 #
# INTRODUCTION TO A&P, VARIABLES AND OPERATORS #
# BY ALEXANDER LEGOLAS MYFIA #
#----------------------------------------------------------------

#%%
# Variables and Data Types

name = "Alexander Legolas Myfia"
age = 19
GPA = 3.97
hasGirlfriend = True

print("----------------------------------------------------------------")
print(f"\nHello! my name is {name} and I am {age} years old.")
print("I have a GPA of " + str(GPA))
print("It is", hasGirlfriend, ", I have a GF\n")
print("----------------------------------------------------------------")

#%%
# Operators
print()

add = 2 + 2
print("Addition\t=", add)

sub = 4 - 2
print("Subtract\t=", sub)

mul = 3 * 2
print("Multiply\t=", mul)

div = 4 / 2
print("Divide\t\t=", div)

exp = 2 ** 3
print("Exponent\t=", exp)

mod = 10 % 7
print("Modulus\t\t=", mod)

maths = add + sub - mul * div / exp ** mod
print("Math operation\t=", maths)

print()
print("----------------------------------------------------------------")
print()

add += 2
print("New Addition\t=", add)

sub -= 1
print("New Subtract\t=", sub)

mul *= 2
print("New Multiply\t=", mul)

div /= 2
print("New Divide\t=", div)

exp **= 2
print("New Exponent\t=", exp)

mod %= 2
print("New Modulus\t=", mod)

print()
print("----------------------------------------------------------------")
print()

more = mul > div
print("Is mul more than div?", more)

less = add < sub
print("Is add less than sub?", less)

equal = sub == div
print("Is sub equal to div?", equal)

same = isinstance(age, int)
print("Is age an integer?", same)