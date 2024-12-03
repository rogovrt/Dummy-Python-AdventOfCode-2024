def find_end_of_num(s : str, i : int):
    while s[i].isdigit():
        i += 1
    return i

def process_line(s : str):
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
                res += num1 * num2
        i = j_end
    return res

res = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        res += process_line(line)
print(res)