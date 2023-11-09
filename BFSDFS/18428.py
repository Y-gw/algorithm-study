import sys

# function

# bfs를 통해 선생님 위치에서 학생 보이는지 탐색
def check_stu() :
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # 선생님 위치
    for i in t :
        # 동, 서, 남, 북 탐색
        for j in range(4) : 
            x, y = i

            while 0 <= x < n and 0 <= y < n :
                # 장애물 발견 시 통과
                if matrix[x][y] == "O" :
                    break

                # 학생이 보인 경우 : 실패
                if matrix[x][y] == "S" :
                    return False

                x += dir[j][0]
                y += dir[j][1]

    # 모든 for문을 통과한 경우(학생이 보이지 않은 경우) : 성공
    return True
    
def obstacle(cnt) :
    global state

    # 장애물 3개 설치
    if cnt == 3 :
        # 선생님 위치에서 학생이 보이지 않는 경우 : 성공
        if check_stu() == True :
            state = True 
            return
    else:
        # 모든 공간에 장애물 설치
        for x in range(n) :
            for y in range(n) :
                if matrix[x][y] == "X" :
                    matrix[x][y] = "O"
                    obstacle(cnt + 1) 
                    matrix[x][y] = "X"

# main
n = int(sys.stdin.readline()) 
state = False
matrix = []
t = []

for i in range(n):
    matrix.append(list(map(str, sys.stdin.readline().split())))
    for j in range(n):
        if matrix[i][j] == "T": 
            t.append([i, j])


obstacle(0)

if state :
    print("YES")
else :
    print("NO")