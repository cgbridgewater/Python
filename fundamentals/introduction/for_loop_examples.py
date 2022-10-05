### 'for loop' examples

## print 0-9
for i in range(10):
    print(i)


## print 3-9
for num in range(3,10):
    print(num)


## print 3-9 increments of 3
for nums in range(3,10,3):
    print(nums)


_list = [{"name":"nathan","age":31}, {"name":"billybob", "age":33}]
## print index + variable
for index in _list:
    print(index)


## print at index + variable
print(_list[0])
## print first index and key 'name'
print(_list[0]["name"])
