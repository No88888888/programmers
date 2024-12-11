from urllib.parse import parse_qs


def solution(ingredient):
    answer = 0
    pattern = [1,2,3,1]
    inLen = len(ingredient)
    po = -1
    while po < inLen-3:
        po += 1
        if po < 0:
            po = 0
        if ingredient[po:po+4] == pattern:
            del ingredient[po:po+4]
            answer += 1
            inLen -= 4
            if len(ingredient) < 4:
                break
            if ingredient[po] == 1:
                po -= 4
            elif ingredient[po] == 2:
                po -= 2
            elif ingredient[po] == 3:
                po -= 3
    return answer
arr = [2, 1, 1, 2, 3, 1, 2, 3, 1]
arr2 = [1, 3, 2, 1, 2, 1, 3, 1, 2]

print(solution(arr2))