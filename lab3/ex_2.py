#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'karl', 'karl', 'Karl', 'Karl']
data2 = gen_random(1, 3, 10)
print ([x for x in gen_random(1,3,5)])
data_list=['kArL','Karl','KARL','KARL','MaRl', 'maRL', 'string','STRING', 'StRINg']
print([x for x in Unique(data1)])
# Реализация задания 2
print([x for x in Unique(gen_random(1,3,5))])
print([x for x in Unique(data_list, ignore_case=True)])
print([x for x in Unique(data_list, ignore_case=False)])