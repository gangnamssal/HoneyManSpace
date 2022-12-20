import sys
sys.stdin = open('이진 힙.txt','r')
# 이진 최소힙에 저장
# 마지막 노드의 조상 노드에 저장된 정수의 합
def heap_push(n):
    global heap_count
    heap_count += 1
    heap[heap_count] = n
    c = heap_count
    p = c // 2
    while heap_count and heap[c] < heap[p]:
        heap[c], heap[p] = heap[p],heap[c]
        c = p
        p = c // 2

# 테스트 케이스의 수
T = int(input())
for tc in range(1,T+1):
    # 테스트 케이스의 별로 N
    N = int(input())
    # 수를 저장할 힙리스트
    heap = [0]*(N+1)
    # 힙의 마지막 인덱스
    heap_count = 0
    # 1000000 이하인 서로 다른 N개의 자연수
    number = list(map(int,input().split()))
    for i in number:
        heap_push(i)
    # 마지막 노드의 조상 노드에 저장된 정수의 합
    sum = 0
    while heap_count > 0:
        heap_count //= 2
        sum += heap[heap_count]

    print(f'#{tc} {sum}')
