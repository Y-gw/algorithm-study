'''
**input**
n = 수의 개수
숫자(A1 ... An)
+ - * //


'''

n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

max_value = -1e10
min_value = 1e10

def dfs(cur, total):
    global max_value, min_value, operators
    if cur == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
    else:
        if operators[0] > 0:
            operators[0] -= 1
            dfs(cur+1, total + numbers[cur])
            operators[0] += 1

        if operators[1] > 0:
            operators[1] -= 1
            dfs(cur+1, total - numbers[cur])
            operators[1] += 1

        if operators[2] > 0:
            operators[2] -= 1
            dfs(cur+1, total * numbers[cur])
            operators[2] += 1

        if operators[3] > 0:
            operators[3] -= 1
            dfs(cur+1, int(total / numbers[cur])) # total // numbers[cur]과의 차이가 뭐지: 아 다르군...
            operators[3] += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)
