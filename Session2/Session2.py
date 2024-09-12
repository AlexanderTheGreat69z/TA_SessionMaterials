#----------------------------------------------------------------
# SESSION 2 #
# INPUT, CONDITIONALS, AND LOOPS #
# BY ALEXANDER LEGOLAS MYFIA #
#----------------------------------------------------------------

#%%
# User Input
name = input("Enter your name: ") 
age = eval(input("Enter your age: "))
print(f"Hello, {name}! You are {age} years old")

print()
print("----------------------------------------------------------------")
print()

#%%
# Conditionals
print("SMASH or PASS?")

if age >= 40: print("u old bruv, pass")
elif age >= 18: print("aight u good, smash")
else: print("FBI, OPEN UP!")

print()
print("----------------------------------------------------------------")
print()

#%%
# Loops
for n in range(1, 10):
    print(f"The square of {n} is {n**2}")
    
print()
print("----------------------------------------------------------------")
print()

arr = ["Alpha", "Bravo", "Gamma", "Zeta"]
for stuff in arr:
    print(f"{stuff} Six, going dark")

print()
print("----------------------------------------------------------------")
print()

countdown = 10
while countdown > 0:
    print(f"{countdown} seconds left")
    countdown -= 1
    