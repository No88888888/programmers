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

        org[i][2] = org[i][0] - org[i][1]

    for p in range(N):
        for q in range(p, N):
            if gift_table[p][q] > gift_table[q][p]:
                answer_arr[p] += 1
            elif gift_table[p][q] < gift_table[q][p]:
                answer_arr[q] += 1
            else:
                if org[p][2] > org[q][2]:
                    answer_arr[p] += 1
                elif org[p][2] < org[q][2]:
                    answer_arr[q] += 1

    answer = max(answer_arr)

    return answer

solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
solution(["joy", "brad", "alessandro", "conan", "david"], ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"])
solution(["a", "b", "c"],["a b", "b a", "c a", "a c", "a c", "c a"])