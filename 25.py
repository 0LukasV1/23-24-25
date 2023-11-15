import random
from collections import Counter

winning_numbers = []
list_of_num = []
final_list = []
for i in range(6):
    winning_numbers.append(random.randrange(1,49))
    print(winning_numbers)


with open ('loteria_2 (1).txt','r', encoding='utf-8') as fp:
    for line in fp:
        line_fin = line.replace('\n','')
        x = line_fin.split(' ')
        for i in x:
            list_of_num.append(int(i))
        # print(list_of_num)
        final_list.append(len(set(list_of_num) & set(winning_numbers)))
        list_of_num = []
    all = Counter(final_list)
    print(all)

    print(final_list)