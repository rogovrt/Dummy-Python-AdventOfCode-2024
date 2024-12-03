import numpy as np

def read_input():
    left_list = []
    right_list = []
    with open('input.txt', 'r') as input_file:
        for line in input_file.readlines():
            left_num, right_num = line.split('   ')
            left_num = (int)(left_num)
            right_num = (int)(right_num)
            left_list.append(left_num)
            right_list.append(right_num)
    return left_list, right_list

ll, rl = read_input()
ll.sort()
rl.sort()

distance_list = np.array(ll) - np.array(rl)
print(np.sum(np.abs(distance_list)))