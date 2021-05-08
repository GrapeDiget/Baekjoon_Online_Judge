def solution(s: str):
    i = 0
    answer = 0
    while i < len(s):
        if s[i].isdigit():
            answer = answer*10+int(s[i])
            i += 1
        elif s[i] == 'z':
            answer = answer*10+0
            i += 4
        elif s[i] == 'o':
            answer = answer*10+1
            i += 3
        elif s[i] == 't' and s[i+1] == 'w':
            answer = answer*10+2
            i += 3
        elif s[i] == 't' and s[i+1] == 'h':
            answer = answer*10+3
            i += 5
        elif s[i] == 'f' and s[i+1] == 'o':
            answer = answer*10+4
            i += 4
        elif s[i] == 'f' and s[i+1] == 'i':
            answer = answer*10+5
            i += 4
        elif s[i] == 's' and s[i+1] == 'i':
            answer = answer*10+6
            i += 3
        elif s[i] == 's' and s[i+1] == 'e':
            answer = answer*10+7
            i += 5
        elif s[i] == 'e':
            answer = answer*10+8
            i += 5
        elif s[i] == 'n':
            answer = answer*10+9
            i += 4

    return answer
