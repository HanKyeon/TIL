'''
N가지 종류의 화폐로 M원을 줘야 한다.
종류별 화폐의 갯수는 무제한일 때, M원을 주는 최소한의 화폐 갯수는?

처음에는 몇가지 종류의 화폐가 있는지 N, 얼마를 만들어줘야하는지 M을 제시.
화폐의 종류를 1이상 10000이하 자연수에서 N개 제시.
최소 화폐 갯수를 출력하며, 불가능 할 시 -1 출력.

dp 테이블에는 인덱스에 해당하는 M원만큼 내줘야 할 화폐의 갯수를 기록.
로직은 x원, k1 k2 k3 kn의 화폐 단위 일 때,
x-k1원에서 k1 한 번 더 주면 되니 d테이블의 d[x-k1] 값에서 1을 더해준 값이 화폐의 갯수
같은 방식으로 x-k2, x-k3, x-k4...x-kn 테이블에서 1 더한값을 비교하여 가장 작은 값.
'''
# n, m 입력
n, m = int(input().split())
# n개의 화폐 단위 입력
arr = []
for i in range(n) :
    arr.append(int(input()))
# dp 테이블 초기화. 훑지 않는 값이 10001을 만들 수 없는 값이라고 가정
d = [10001] * (m + 1)
# 0원은 0개의 화폐로 가능. 초기값 초기화.
d[0] = 0
# bottom up dp.
# 목표한 가격인 i원을 거슬러 주는 화폐의 갯수는
# 화폐의 종류별로 1씩 뺀 값의 d[i-화폐]에서 1을 더한 값이 i원을 거슬러 줄 때 필요한 화폐 갯수이다.
# 따라서 화폐 종류를 순회해야 하며, dp값 저장을 위해 i만큼 또 돌아야 해서 2중 for문이 된다.
for i in range(n) :
    for j in range(arr[i], m+1) :
        if d[j - arr[i]] != 10001 : # (1-k)원을 만드는 방법이 있는 경우.
                                    # 화폐의 모든 종류를 빼보았는데 d값이 10001이면 줄 수 없음.
            d[j] = min(d[j], d[j - arr[i]]+1)
# 만약 거슬러 줄 수 없으면 -1을 출력.
if d[m] == 10001 :
    print(-1)
else :
    print(d[m])

