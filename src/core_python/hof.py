def return_sum(func, list):
    result = 0
    for i in list:
        if func(i):
            result += i
    return result

even = lambda x: x%2 == 0
odd = lambda x: x%2 != 0
div3 = lambda x: x%3 == 0

random_list = [11, 14, 21, 23, 56, 78, 45, 29, 28]

print(return_sum(even, random_list))
print(return_sum(odd, random_list))
print(return_sum(div3, random_list))
