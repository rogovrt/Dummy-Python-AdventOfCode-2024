def handle_differs(differs : list) -> int:
    i = 0
    while (i <= len(differs) - 1) and (abs(differs[i]) > 0) and (abs(differs[i]) < 4) and (not ((differs[0] > 0) ^ (differs[i] > 0))):
        i += 1
    return i


def process_report(report_str : str) -> bool:
    levels_str = report_str.split(' ')
    levels_int = list(map(int, levels_str))
    differs = []
    for i in range(len(levels_int) - 1):
        differs.append(levels_int[i + 1] - levels_int[i])
    i = handle_differs(differs)
    if i == len(differs):
        return True
    else:
        for i in range(len(differs)):
            if i == 0 and handle_differs(differs[1:]) == len(differs) - 1:
                return True
            elif i == len(differs) - 1:
                return handle_differs(differs[:-1]) == len(differs) - 1
            else:
                corrected_differs = []
                for j in range(i):
                    corrected_differs.append(differs[j])
                corrected_differs.append(differs[i] + differs[i + 1])
                for j in range(i + 2, len(differs)):
                    corrected_differs.append(differs[j])
                if handle_differs(corrected_differs) == len(corrected_differs):
                    return True


res = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        res += process_report(line)
print(res)