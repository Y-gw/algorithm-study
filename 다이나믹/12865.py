import sys
input = sys.stdin.readline
 
n,k = map(int,input().split())
items = []

for i in range(n):
    w,v = map(int,input().split()) # 무게,가치 입력받음
    items.append((w,v)) # items 리스트에 저장

dp = [0 for _ in range(k+1)] # dp 리스트 생성

for i in items:
    w,v = i
    for j in range(k,w-1,-1): # 중복을 피해서 저장하기 위해 k부터
        dp[j] = max(dp[j],dp[j-w]+v) # j가 k부터 k-1, k-2, ..., w까지

print(dp[k]) #k에 해당하는 값