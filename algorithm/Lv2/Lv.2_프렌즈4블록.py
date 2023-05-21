'''
문제 설명
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 이번에 출시할 게임 제목은 "프렌즈4블록".
같은 모양의 카카오프렌즈 블록이 2×2 형태로 4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.

board map
만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.

board map

블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.

board map

만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 모이면 다시 지워지고 떨어지고를 반복하게 된다.
board map

위 초기 배치를 문자로 표시하면 아래와 같다.

TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
각 문자는 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)을 의미한다

입력으로 블록의 첫 배치가 주어졌을 때, 지워지는 블록은 모두 몇 개인지 판단하는 프로그램을 제작하라.

입력 형식
입력으로 판의 높이 m, 폭 n과 판의 배치 정보 board가 들어온다.
2 ≦ n, m ≦ 30
board는 길이 n인 문자열 m개의 배열로 주어진다. 블록을 나타내는 문자는 대문자 A에서 Z가 사용된다.
출력 형식
입력으로 주어진 판 정보를 가지고 몇 개의 블록이 지워질지 출력하라.
'''

def solution(m, n, board):
    answer = 0
    arr = [[0]*m for _ in range(n)]     # 편의를 위해 오른쪽으로 90도 회전한 배열을 받기 위한 arr
    for i in range(n):
        for j in range(m):
            arr[i][j] = board[m-1-j][i] # 90도 회전해서 받는다
    
            
    def dfs(x, y, blo):             # 4칸 탐색 함수
        temp = [(x,y)]              # 탐색 시작 칸
        for di, dj in delta:        # 우, 우하, 하 3방 탐색
            ni, nj = x + di, y + dj
            if 0 <= ni < n and 0 <= nj < m and blo == arr[ni][nj]:  # 범위내고 같은 캐릭터라면
                temp.append((ni,nj))    # temp에 넣는다
            else:                   # 한번이라도 기준 충족 안한다면
                return              # 바로 탐색 종료
        stack.extend(temp)          # 4칸 모두 같은 캐릭터라면 stack에 해당 칸들을 일단 넣는다(전체 탐색 후 한번에 지우기 위함)

        
    delta = (0,1), (1,1), (1,0)         # 3방 탐색 위한 delta
    end = 0                             # 탐색을 끝낼지 말지 결정할 flag 
    while not end: 
        stack = []
        for i in range(n):              # 전체 탐색
            for j in range(m):
                if arr[i][j]:           # 빈칸이 아니라면
                    dfs(i, j, arr[i][j])# 해당 칸에서 탐색 시작
                    
        if not stack:                   # 지울 칸이 없다면
            end = 1                     # 종료
            break
        else:                           # 지울 칸이 있다면
            stack = list(set(stack))    # 지울 칸 중 중복되는 칸이 있을 수 있기 때문에 set으로 정리 
            while stack:                
                x, y = stack.pop()  
                arr[x][y] = 0           # 지울 칸을 0으로 만듦
                answer += 1             # 지움 횟수 + 1
            for li in arr:              # 0인 칸을 remove
                while 0 in li:
                    li.remove(0)
            for li in arr:              # 삭제하고 부족한 칸만큼 뒤에 0을 채움
                while len(li) < m:
                    li.append(0)
            
    return answer

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])