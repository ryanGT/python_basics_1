mydict = {'a':'hello', 'b':'ryan'}
mykeys = mydict.keys()# get the keys
print('mykeys = ' + str(mykeys))
myvalues = mydict.values()# get the values
print('myvalues = ' + str(myvalues))

a_val = mydict['a']# use indexing to extract an item
b_val = mydict['b']# and another

# once the dictionary has been created, you can insert
# new items like this:
mydict['b2'] = 7.0

# you can iterate of the keys and values in a for loop like this:
for key, value in mydict.items():
    print('key = %s, value = %s' % (key, value))
