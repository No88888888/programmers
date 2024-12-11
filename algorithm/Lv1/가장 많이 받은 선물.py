from collections import defaultdict

def solution(friends, gifts):
    N = len(friends)
    numbering_table = {}
    gift_table = [[0]*N for _ in range(N)]
    org = [[0]*3 for _ in range(N)]
    num = -1
    for fr in friends:
        num += 1
        numbering_table[fr] = num
    for g in gifts:
        dp = g.split(" ")[0]
        ar = g.split(" ")[1]
        gift_table[numbering_table[dp]][numbering_table[ar]] += 1

    answer_arr = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            org[i][0] += gift_table[i][j]
            org[i][1] += gift_table[j][i]
            org[j][1] += gift_table[j][i]
            org[j][0] += gift_table[i][j]

        org[i][2] = org[i][0] - org[i][1]
        org[j][2] = org[j][0] - org[j][1]
        if gift_table[i][j] > gift_table[j][i]:
            answer_arr[i] += 1
        elif gift_table[i][j] < gift_table[j][i]:
            answer_arr[j] += 1
        else:
            pass
    for k in range(N):

    answer = 0
    return answer

solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])