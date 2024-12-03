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
num_occur_dict = {}
rl.sort()
res = 0

for num in ll:
    if num not in num_occur_dict.keys():
        occurences = 0
        for i in range(len(rl)):
            if num == rl[i]:
                occurences += 1
            elif num < rl[i]:
                break
        num_occur_dict[num] = occurences
    res += num * num_occur_dict[num]
print(res)