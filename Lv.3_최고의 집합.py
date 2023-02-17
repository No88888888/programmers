'''
문제 설명
자연수 n 개로 이루어진 중복 집합(multi set, 편의상 이후에는 "집합"으로 통칭) 중에 다음 두 조건을 만족하는 집합을 최고의 집합이라고 합니다.

각 원소의 합이 S가 되는 수의 집합
위 조건을 만족하면서 각 원소의 곱 이 최대가 되는 집합
예를 들어서 자연수 2개로 이루어진 집합 중 합이 9가 되는 집합은 다음과 같이 4개가 있습니다.
{ 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 }
그중 각 원소의 곱이 최대인 { 4, 5 }가 최고의 집합입니다.

집합의 원소의 개수 n과 모든 원소들의 합 s가 매개변수로 주어질 때, 최고의 집합을 return 하는 solution 함수를 완성해주세요.

제한사항
최고의 집합은 오름차순으로 정렬된 1차원 배열(list, vector) 로 return 해주세요.
만약 최고의 집합이 존재하지 않는 경우에 크기가 1인 1차원 배열(list, vector) 에 -1 을 채워서 return 해주세요.
자연수의 개수 n은 1 이상 10,000 이하의 자연수입니다.
모든 원소들의 합 s는 1 이상, 100,000,000 이하의 자연수입니다.
입출력 예
n	s	result
2	9	[4, 5]
2	1	[-1]
2	8	[4, 4]
입출력 예 설명
입출력 예#1
문제의 예시와 같습니다.

입출력 예#2
자연수 2개를 가지고는 합이 1인 집합을 만들 수 없습니다. 따라서 -1이 들어있는 배열을 반환합니다.

입출력 예#3
자연수 2개로 이루어진 집합 중 원소의 합이 8인 집합은 다음과 같습니다.

{ 1, 7 }, { 2, 6 }, { 3, 5 }, { 4, 4 }

그중 각 원소의 곱이 최대인 { 4, 4 }가 최고의 집합입니다.
'''
# from itertools import permutations
# def solution(n, s):
#     arr = []
#     answer = []
#     for i in (permutations([i for i in range(10000)], n)):
#         if sum(i) == s:
#             arr.append(i)
#     maxx= 0
#     for x in arr:
#         temp = 1
#         for j in x:
#             temp = temp * j
#         if temp > maxx:
#             answer = [list(x)]
#             maxx = temp
#     print(answer)
#     return answer

'''
합이 s가 되는 자연수 n개의 조합 중 각 수들의 곱이 최대가 되는 경우는
각 수들의 차가 최소가 되는 조합이다
s를 n으로 나눈 몫과 나머지를 이용하여 푸는 방식으로 접근한다
'''
def solution(n,s):
    if s%n == 0:        # 나머지가 없다면(나눠 떨어진다면) 
        A = s//n    
        answer = [A]*n  # 몫 A가 n개로만 이뤄진 조합이 답
    elif s//n == 0:     # 몫이 0이라면    
        answer = [-1]   # 조합 불가능
    else:               # 나머지가 있다면(나눠 떨어지지 않는다면)
        A = s//n        # 몫   
        B = s%n         # 나머지
        answer = [A]*(n-B)  # 전체개수에서 나머지만큼 뺀 개수만큼 A를 채우고
        plus = [A+1]*B      # (나머지 B를 A네게 1씩 나눠 더해준다) * B 개수
        answer.extend(plus) # 답 배열 뒤에 추가해준다
    return answer

solution(4, 10)
solution(2, 9)
solution(2, 1)
solution(2, 8)