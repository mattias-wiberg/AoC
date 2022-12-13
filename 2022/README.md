Day 11: Maybe python bug but worth noting: 
``
a = []
b = lambda old: eval('old*5')
a.append(b)
# a[0](1) == 5
b = lambda old: eval('old+1')
a.append(b)
# a[0](1): 2 !!
# a[1](1): 2
``
Have to do:
``
a = []
b = eval('lambda old: old*5')
a.append(b)
# a[0](1) == 5
b = eval('lambda old: old+1')
a.append(b)
# a[0](1): 5
# a[1](1): 2
``
The least common multiple (lcm) can be used to reduce numbers without loosing any divisible information.