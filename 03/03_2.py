def find_end_of_num(s : str, i : int):
    while s[i].isdigit():
        i += 1
    return i

def find_all_indexes_of_pattern(s : str, pattern : str):
    i = 0
    inds = []
    while s.find(pattern, i) != -1:
        pattern_start_ind = s.find(pattern, i)
        inds.append(pattern_start_ind)
        i = pattern_start_ind + len(pattern)
    return inds

def find_closest_in_list(num, list):
    if list[0] > num:
        return -1
    if num > list[-1]:
        return list[-1]
    for i in range(len(list) - 1):
        if num > list[i] and num < list[i + 1]:
            return list[i]

def process_line(s : str):
    do_pattern = "do()"
    do_inds = find_all_indexes_of_pattern(s, do_pattern)
    dont_pattern = "don't()"
    dont_inds = find_all_indexes_of_pattern(s, dont_pattern)

    i = 0
    res = 0
    base_patter = "mul("
    while i < len(s) - 4 or s.find(base_patter, i) != -1:
        j_start = s.find(base_patter, i)
        j_start += 4
        j_end = find_end_of_num(s, j_start)
        if s[j_end] == ',':
            num1 = (int)(s[j_start:j_end])
            j_start = j_end + 1
            j_end = find_end_of_num(s, j_start)
            if s[j_end] == ')':
                num2 = (int)(s[j_start:j_end])
                do_closest = find_closest_in_list(j_end, do_inds)
                dont_closest = find_closest_in_list(j_end, dont_inds)
                if dont_closest != -1 and do_closest == -1:
                    flag = False
                elif dont_closest == -1:
                    flag = True
                elif dont_closest != -1 and do_closest != -1:
                    flag = j_end - dont_closest > j_end - do_closest
                print(f'{flag} : {num1},{num2}')
                if flag:
                    res += num1 * num2
        i = j_end
    return res

res = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        res += process_line(line)
print(res)