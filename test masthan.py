name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age <=18:
    print("{} can cast vote not eliglible this year!".format(name))
else:
    print("{} can cast vote eligible this year!". format(name,18-age))

