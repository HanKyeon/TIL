'''
AC

R D
R은 reversed D는 pop(0)

입력
테케T
함수P 1이상 10만이하
배열 수 n
[배,열,정,수] 1이상 100이하
전체 테케에 주어지는 p 길이 합과 n의 합은 70만 이하.

출력
수행결과. 에러 시 error 출력
'''
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mr = input().rstrip() # 명령
    n = int(input()) # 배열의 길이
    nl = [0] * n
    s = input().rstrip()[1:-1]
    
    



