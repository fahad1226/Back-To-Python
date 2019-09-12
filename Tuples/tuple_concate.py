

tuple1 = (10,20,30,40)

tuple2 = (50,60,70,80)

concate =  tuple2 + tuple1

print(concate)

concate_again = concate + (1,2,3,45,6)
concate_again_with_string = concate_again + ('fahad','susmoy','ishmam','enan','ashim')

print(concate_again)

for member in concate_again_with_string:

    print(member)