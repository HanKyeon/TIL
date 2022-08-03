'''
떡 자르기

떡 N개
떡의 길이가 일정하지 않다.
떡을 잘라서 잘려진 부분을 판다.

요청한 길이가 M일 때, 적어도 M 길이만큼의 떡을 얻기 위해
절단기에 설정 할 수 있는 높이의 최댓값을 구하는 프로그램

떡의 갯수와 요청 받은 떡의 길이.
떡은 1개 이상 100만개 이하
요청 받은 양은 1이상 20억 이하
이후 떡의 개별 높이가 주어짐. 떡 높이의 총합은 항상 M 이상. 높이는 0이상 10억 이하.

입력
4 6
19 15 10 17

출력
15

해당 문제는 이진 탐색으로 풀 수 있다. 떡의 높이에 따라 얻어지는 양이 정렬된 리스트 같기 때문.
중간값 만큼 잘라서 떡을 얻을 수 있는가? 
Yes -> 더 높은 위치에서 자르자
No -> 더 낮은 위치에서 자르자
이런 식으로 이진 탐색이 가능하다.

요청 받은양이 몇억개인 이상, 무조건 이진탐색 고려해야 한다.
'''
# n, m 입력
n, m = list(map(int, input().split(' ')))
# 떡의 높이 개별 정보 입력
arr = list(map(int, input().split()))

# 시작점은 자르는 위치를 0일 때와, 가장 긴 떡 위치를 자를 때 end
start = 0
end = max(arr)

result = 0
# 조건은 이진탐색과 같음.
while(start <= end) :
    # 잘랐을 때 나오는 떡의 양
    total = 0
    # 중앙값은 이진 탐색과 동일
    mid = (start + end) // 2
    # 떡 길이를 훑는데
    for x in arr :
        # 떡이 자를 수 있도록 중간값보다 길면 잘라서
        # 나오는 떡의 양에 더한다.
        if x > mid :
            total += x - mid
    # 만약 떡의 양이 손님이 요구한거보다 적다면
    if total < m :
        # 더 많이 잘라야 하므로, 양이 늘어나기 위해 좌측으로 이동.
        end = mid - 1
    # 떡의 양이 넘친다면, 덜 잘라야 하므로 우측 탐색.
    else :
        result = mid # 떡의 양이 충분하므로 일단 result의 값을 mid로 기록.
                    # 반복하면서 더 높은 곳에서 짤랐을 때 값이 나오면 다시 기록하니까.
        start = mid + 1

print(result)



