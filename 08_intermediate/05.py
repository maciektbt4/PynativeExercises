from random import sample
from unittest import result


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
results = []
for el in sample_list:
    if sample_list.count(el) > 1 and el not in results:
        results.append(el)

print(sorted(results))