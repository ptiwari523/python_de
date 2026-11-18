my_list = [20, 10, 5, 25, 45, 6, 76, 9, 8, 3, 21, 30] # my_list is is an iterable 

# print(dir(my_list))

it = iter(my_list) # it is an iterator

while True:
    try:
        i = next(it)
        print(i)
    except StopIteration:
        break 
