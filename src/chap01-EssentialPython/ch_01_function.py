## Lambda

items = [[0, 'a', 2], [5, 'b',0 ], [2, 'c', 1]]
print(sorted(items))

def second(item):
    return item[2]

print(sorted(items, key=second))
print(sorted(items, key=lambda item: item[1]))
print(sorted(items, key=lambda item: item[2]))