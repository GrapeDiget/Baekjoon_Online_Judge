import collections


def smallsolution(room):
    visited = [[0]*5 for i in range(5)]
    queue = collections.deque()
    for i in range(5):
        for j in range(5):
            if room[i][j] == 'O' or room[i][j] == 'X':
                continue
            if visited[i][j] == 1:
                continue
            visited[i][j] = 1
            queue.append([(i, j), 0])
            while queue:
                [(now_x, now_y), dist] = queue.popleft()
                if now_x > 0 and room[now_x-1][now_y] != 'X' and not visited[now_x-1][now_y]:
                    if room[now_x-1][now_y] == 'O':
                        queue.append([(now_x-1, now_y), dist+1])
                    elif dist < 2:
                        return 0
                    else:
                        queue.append([(now_x-1, now_y), 0])
                if now_y < 4 and room[now_x][now_y+1] != 'X' and not visited[now_x][now_y+1]:
                    if room[now_x][now_y+1] == 'O':
                        queue.append([(now_x, now_y+1), dist+1])
                    elif dist < 2:
                        return 0
                    else:
                        queue.append([(now_x, now_y+1), 0])
                if now_x < 4 and room[now_x+1][now_y] != 'X' and not visited[now_x+1][now_y]:
                    if room[now_x+1][now_y] == 'O':
                        queue.append([(now_x+1, now_y), dist+1])
                    elif dist < 2:
                        return 0
                    else:
                        queue.append([(now_x+1, now_y), 0])
                if now_y > 0 and room[now_x][now_y-1] != 'X' and not visited[now_x][now_y-1]:
                    if room[now_x][now_y-1] == 'O':
                        queue.append([(now_x, now_y-1), dist+1])
                    elif dist < 2:
                        return 0
                    else:
                        queue.append([(now_x, now_y-1), 0])

    return 1


def solution(places):
    answer = list()
    for room in places:
        answer.append(smallsolution(room))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
                                                                                                               "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
