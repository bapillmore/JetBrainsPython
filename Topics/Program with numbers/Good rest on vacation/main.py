duration = int(input())
food = int(input())
flight = int(input())
hotel = int(input())
total = food * duration + flight * 2 + hotel * (duration-1)
print(total)
