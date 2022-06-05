# 제너레이터
def count():
    n = 0
    while n < 5:
        n += 1
        yield n


counter = count()
print(counter)
for c in counter:
    print(c)

# 제너레이터 내포
list_o_nums = [x for x in range(1000)]
gen_o_nums = (x for x in range(1000))

import sys

print(sys.getsizeof(list_o_nums))
print(sys.getsizeof(gen_o_nums))
