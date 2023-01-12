from urllib.parse import parse_qs


def solution(ingredient):
    answer = 0
    pattern = '1231'
    target =  ''.join(map(str, ingredient))
    for i in range(len(target)-len(pattern)+1):
        if target[i:i+4] == pattern:
            answer += 1
    return answer

arr = [2, 1, 1, 2, 3, 1, 2, 3, 1]

print(solution(arr))