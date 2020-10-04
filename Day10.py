angle = int(input("Enter the angle inbetween -180 and 180."))

if -180 >= angle or angle <= 180:
    new_value = 180 + angle
    print(new_value)
else:
    print("Please retry:")


_time = int(input("Enter the time in seconds"))
minitue = _time // 60
seconds = _time % 60
print(minitue)
print(seconds)
print("Minitue = " + str(minitue) + " " + "Second = " + str(seconds))


hour = int(input("Enter the hour in-between 1 and 12"))
if 1 >= hour or hour  <= 12:
    future_hour = int(input("How many hour into future?"))
    new_hour = (hour + future_hour) % 12
    print("New hour: " + str(new_hour))
else:
    print("Retry!")


x = int(input("ENter the number:"))
y = 2 ** x
z = y % 10
a = y % 100
print(z)
print(a)

_base = int(input("Enter base: "))
_power = int(input("Enter the power: "))
y = _base ** _power
z = y % 100
print(z)

