# Declaring variables
name = "Abi"
salary = 60000
age = 30
isMarried = True
test = "True"

# Printing variable
print("Hello World " + name)

print("My salary type is ", type(salary))

# Conditional statements

if name == "Abi":
    print("Matching")
else:
    print("Not Matching")

if age < 10:
    print("Child")
elif age > 10 and age < 18:
    print("Minor")
elif age > 18 and age <= 30:
    print("Youth")
else:
    print("Adult")

# String Array Declration
browsers = ["Chrome", "Safari", "Firefox", "IE", "Opera"]

print("size of browser", browsers.__len__())

print("first browser", browsers[0])

# poppedValue = browsers.pop()
#
# print("Popped value", poppedValue)
#
# print(browsers)
#
# browsers.sort()
#
# print(browsers)

# Looping Statements
for browser in browsers:
    print("Displaying browser name", browser)

# Dictionary
configs = {
    "token": "AAA",
    "id": "123",
    "username": "Rohit",
    "login": True
}

print("first config value", configs["token"])

print("first config value", configs.get("token"))

for key in configs:
    print("key is ", key, "and value is ", configs.get(key))

for value in configs.values():
    print("value is ", value)
