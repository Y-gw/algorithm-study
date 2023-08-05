melon = int(input())

h = 0
w = 0
h_idx = 0
w_idx = 0

total = []   # 모든 변의 정보를 저장할 리스트

for i in range(6):
    temp = list(map(int, input().split()))
    total.append(temp)

    if temp[0] == 1 or temp[0] == 2:   # 동쪽 or 서쪽
        if w < temp[1]:
            w = temp[1]
            w_idx = i
    else:
        if h < temp[1]:
            h = temp[1]
            h_idx = i
    
idx_list = [total[h_idx - 1], total[(h_idx + 1) % 6],
             total[w_idx - 1], total[(w_idx + 1) % 6]]

small = 1
for i in total:
    if i not in idx_list:
        small *= i[1]

result = (w * h - small) * melon
print(result)



'''
2477_참외밭

- 문제풀이 핵심 아이디어
가장 긴 세로 및 가로 길이를 곱한 뒤 가장 긴 변과 인접하지 않은 나머지 2개의 변으로 
사각형의 넓이를 구해서 빼주면 전체 밭의 넓이를 구할 수 있음.

- 시간복잡도
O(1) 모두 상수번의 연산만 진행.
'''