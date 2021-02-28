T = int(input())
R = []
S = []
for i in range(T):
    input_list = input().split()
    R.append(input_list[0])
    S.append(input_list[1])

for i in range(T):
    for j in range(len(S[i])):
        for k in range(int(R[i])):
            print(S[i][j], end="")
    print("")


# 구현