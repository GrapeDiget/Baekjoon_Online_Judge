def smallsolution(room: list):
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'O' or room[i][j] == 'X':
                continue
            for k in range(max(0, i-2), min(4, i+2)+1):
                for l in range(max(0, j-2), min(4, j+2)+1):
                    if abs(i-k)+abs(j-l) > 2:
                        continue
                    if abs(i-k)+abs(j-l) == 0:
                        continue
                    if room[k][l] == 'O' or room[k][l] == 'X':
                        continue
                    if abs(i-k)+abs(j-l) == 1:
                        return 0
                    if abs(i-k) == 2:
                        if i > k:
                            if room[i-1][j] != 'X':
                                return 0
                            else:
                                continue
                        if i < k:
                            if room[i+1][j] != 'X':
                                return 0
                            else:
                                continue
                    if abs(j-l) == 2:
                        if j > l:
                            if room[i][j-1] != 'X':
                                return 0
                            else:
                                continue
                        if j < l:
                            if room[i][j+1] != 'X':
                                return 0
                            else:
                                continue
                    if i > k and j > l:
                        if room[i-1][j] == 'X' and room[i][j-1] == 'X':
                            continue
                        else:
                            return 0
                    if i > k and j < l:
                        if room[i-1][j] == 'X' and room[i][j+1] == 'X':
                            continue
                        else:
                            return 0
                    if i < k and j > l:
                        if room[i+1][j] == 'X' and room[i][j-1] == 'X':
                            continue
                        else:
                            return 0
                    if i < k and j < l:
                        if room[i+1][j] == 'X' and room[i][j+1] == 'X':
                            continue
                        else:
                            return 0

    return 1


def solution(places):
    answer = list()
    for room in places:
        answer.append(smallsolution(room))

    return answer


print(solution([[
    "PXPOO",
    "XPXOO",
    "PXPXO",
    "XPXPO",
    "OPOOO"]]))