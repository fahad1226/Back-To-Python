
tuple1 = (10,20,30,40)

tuple_rpt = tuple1 * 4

print(tuple_rpt)

print( tuple_rpt[-3] )

print( tuple_rpt[3:6] )

print( 10 in tuple_rpt )


if 40 in tuple_rpt:

    print( tuple_rpt.index(40) )



print( 1000 not in tuple_rpt )
print( 10 not in tuple_rpt )

print( len(tuple_rpt) )


print( max(tuple_rpt) )
print( min(tuple_rpt) )