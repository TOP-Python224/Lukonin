from random import randrange as rr

list1 = [rr(0, 50, 5) for _ in range(5)]
list2 = [rr(0, 50, 5) for _ in range(5)]

print(list1, list2, sep='\n', end='\n\n')

for num in set(list1) & set(list2):
    for item in (list1, list2):
        for i in range(item.count(num)):
            item.remove(num)
print(list1, list2, sep='\n')
