import sys
input = sys.stdin.readline

for t in range(int(input())):
    N, C = map(int, input().split())
    if C > N*(N+1)//2-1 or C < N-1:
        print(f"Case #{t+1}: IMPOSSIBLE")
        continue
    L = list(range(1, N+1))
    C -= N-1
    left = 0
    right = N-1
    for num in range(1, N+1):
        if C - (N-num) >= 0:
            C -= N-num
            if num%2 == 0:
                L[left:right+1] = reversed(L[left:right+1])
                left += 1
            else:
                L[left:right+1] = reversed(L[left:right+1])
                right -= 1
            continue
        if num%2 == 0:
            L[right-C:right+1] = reversed(L[right-C:right+1])
        else:
            L[left:left+C+1] = reversed(L[left:left+C+1]) 
        break
    
    print(f"Case #{t+1}: {' '.join(map(str, L))}")