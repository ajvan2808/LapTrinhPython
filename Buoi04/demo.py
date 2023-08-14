week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
e = enumerate(iterable=week, start=2)
print('e:', e)
print(list(e))

'''
# print(list(e))
for item in list(e):
    print(item)
    
The for loop cannot print because the list list(e) does not contain any elements. 
The enumerate() function returns a generator, which is a special type of iterator 
that does not store all of its elements in memory at once. 
Instead, it generates the elements one at a time as they are needed. 
The list() function takes a generator and converts it to a list, which stores all of the elements in memory. 
However, in this case, the generator list(e) does not contain any elements, so the list is empty.

We can try print list(e) one more time to verify and the output is an empty list.
'''

ds = ['a', 'h', 'k', 1, 6.8]
print(dict(enumerate(ds)))

for i, value in enumerate(ds):
    print(i, '-', value)


print('----------------- FILTER FUNCTION ------------------------')


def xet_chan(x):
    if x%2 == 0:
        return True
    return False


foo = [1, 2, 3, 4, 5, 6, 7, 8, 9]

rs = filter(xet_chan, foo)
print(list(rs))

print('----------------- SORTED FUNCTION ------------------------')
print(sorted(foo, reverse=True))


print('----------------- MAP FUNCTION ------------------------')


def cong_nam(y):
    return y + 5


kq = list(map(cong_nam, foo))
print(kq)
