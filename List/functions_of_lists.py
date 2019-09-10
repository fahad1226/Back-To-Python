
#functions are  -->>

# extended()
# pop()
# remove()
# insert(index,value)
# clear()
# push()
# appened()
#count(value)  returns how many time a value has in a list
#index(value)  return index number
#sort()
#reverse()


lucky_numbers = [10,20,34,54,12,26]

unlucky_numbers = [-10,-20,-34,-54,-12,-26]

unlucky_numbers.insert(2,2000)

print(unlucky_numbers)

unlucky_numbers.append(-375463)

unlucky_numbers.extend(lucky_numbers)

print(unlucky_numbers)
print(lucky_numbers)
lucky_numbers.remove(12)
print(lucky_numbers)
print(unlucky_numbers)
unlucky_numbers.clear()

print(unlucky_numbers)

friends = ["fahad","John","hopper","fahad","will"]

indx = friends.index("will")

friends2 = friends.copy()

print(friends2)
print(indx)

print( friends.count("fahad") )

friends.sort()

print(friends)