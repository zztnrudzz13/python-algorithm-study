#incomplete - DP 적용해서 풀어야 함

from collections import deque

str_list = list(input())
before_result = []
result = deque()

# 1이랑 3비교
def check_both(left, right):
    if left < 0 or right > len(str_list) - 1:
        print('hello')
        return before_result
    if str_list[left] == str_list[right]:
        result.appendleft(str_list[left])
        result.append(str_list[right])
        check_both(left - 1, right + 1)
    else:
        if len(result) >= len(before_result):
            before_result.clear()
            before_result.append(result)
            print(before_result)
            result.clear()
            return before_result


for i in range(1, len(str_list)):
    current = str_list[i]
    left = i - 1  # 0
    right = i + 1  # 2
    if left < 0 or right == len(str_list):
        break
    print(str_list[left], current, str_list[right])
    if str_list[left] == str_list[right]:
        result.append(str_list[left])
        result.append(current)
        result.append(str_list[right])
        if left == 0 or right == len(str_list) - 1:
            before_result.append(result)
            result.clear()
        else:
            check_both(left - 1, right + 1)
    elif str_list[left] == current:
        result.append(str_list[left])
        result.append(current)
        if left == 0 or i == len(str_list) - 1:
            before_result.append(result)
            result.clear()
        else:
            check_both(left - 1, i + 1)
    elif str_list[right] == current:
        result.append(current)
        result.append(str_list[right])
        if i == 0 or right == len(str_list) - 1:
            before_result.append(result)
            result.clear()
        else:
            check_both(i - 1, right + 1)
    else:
        continue

print(before_result)