#----------------------------------------------------------------
# SESSION 3 #
# LISTS, TUPLES, AND DICTIONARIES #
# BY ALEXANDER LEGOLAS MYFIA #
#----------------------------------------------------------------

#%%
lis = [1, 2, 3, 4, 5, 'Yes', 'no', 'sandwich', True, 6.28]
for i in lis:
    print(i)

print(lis[4])
lis.remove('no')
print(lis)

lis.append("Prabowo")
print(lis)

print(lis.index('sandwich'))
#%%
tup = (255, 255, 255)
for i in tup:
    print(i)

#%%
MyDict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
    "hobbies": ["reading", "painting", "cooking"],
    "favouritenum": (69, 420, 1080),
    "dictionary": {"code" : 1945}
}

MyDict.pop("city")
MyDict["food"] = "sausage"
print(MyDict)


eval()