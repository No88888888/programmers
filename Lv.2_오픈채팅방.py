'''
���� ����
����ä�ù�
īī���� ����ä�ù濡���� ģ���� �ƴ� ������ ��ȭ�� �� �� �ִµ�, ���� �г����� �ƴ� ������ �г����� ����Ͽ� ä�ù濡 �� �� �ִ�.

���Ի���� ��ũ��� īī���� ���� ä�ù��� ������ ����� ����, �پ��� ������� ������, ������ ���� ���Ѻ� �� �ִ� ������â�� ������ �ߴ�. ä�ù濡 ������ ������ ���� �޽����� ��µȴ�.

"[�г���]���� ���Խ��ϴ�."

ä�ù濡�� ������ ������ ���� �޽����� ��µȴ�.

"[�г���]���� �������ϴ�."

ä�ù濡�� �г����� �����ϴ� ����� ������ ���� �� �����̴�.

ä�ù��� ���� ��, ���ο� �г������� �ٽ� ����.
ä�ù濡�� �г����� �����Ѵ�.
�г����� ������ ���� ������ ä�ù濡 ��µǾ� �ִ� �޽����� �г��ӵ� ���� ����ȴ�.

���� ���, ä�ù濡 "Muzi"�� "Prodo"��� �г����� ����ϴ� ����� ������� ������ ä�ù濡�� ������ ���� �޽����� ��µȴ�.

"Muzi���� ���Խ��ϴ�."
"Prodo���� ���Խ��ϴ�."

ä�ù濡 �ִ� ����� ������ ä�ù濡�� ������ ���� �޽����� ���´�.

"Muzi���� ���Խ��ϴ�."
"Prodo���� ���Խ��ϴ�."
"Muzi���� �������ϴ�."

Muzi�� ������ �ٽ� ���� ��, Prodo ��� �г������� ���� ��� ������ ä�ù濡 �����ִ� Muzi�� Prodo�� ������ ���� ����ȴ�.

"Prodo���� ���Խ��ϴ�."
"Prodo���� ���Խ��ϴ�."
"Prodo���� �������ϴ�."
"Prodo���� ���Խ��ϴ�."

ä�ù��� �ߺ� �г����� ����ϱ� ������, ���� ä�ù濡�� Prodo��� �г����� ����ϴ� ����� �� ���� �ִ�. ����, ä�ù濡 �� ��°�� ���Դ� Prodo�� Ryan���� �г����� �����ϸ� ä�ù� �޽����� ������ ���� ����ȴ�.

"Prodo���� ���Խ��ϴ�."
"Ryan���� ���Խ��ϴ�."
"Prodo���� �������ϴ�."
"Prodo���� ���Խ��ϴ�."

ä�ù濡 ������ �����ų�, �г����� ������ ����� ��� ���ڿ� �迭 record�� �Ű������� �־��� ��, ��� ����� ó���� ��, ���������� ���� ������ ����� ���� �Ǵ� �޽����� ���ڿ� �迭 ���·� return �ϵ��� solution �Լ��� �ϼ��϶�.

���ѻ���
record�� ������ ���� ���ڿ��� ��� �迭�̸�, ���̴� 1 �̻� 100,000 �����̴�.
������ record�� ��� ���ڿ��� ���� �����̴�.
��� ������ [���� ���̵�]�� �����Ѵ�.
[���� ���̵�] ����ڰ� [�г���]���� ä�ù濡 ���� - "Enter [���� ���̵�] [�г���]" (ex. "Enter uid1234 Muzi")
[���� ���̵�] ����ڰ� ä�ù濡�� ���� - "Leave [���� ���̵�]" (ex. "Leave uid1234")
[���� ���̵�] ����ڰ� �г����� [�г���]���� ���� - "Change [���� ���̵�] [�г���]" (ex. "Change uid1234 Muzi")
ù �ܾ�� Enter, Leave, Change �� �ϳ��̴�.
�� �ܾ�� �������� ���еǾ� ������, ���ĺ� �빮��, �ҹ���, ���ڷθ� �̷�����ִ�.
���� ���̵�� �г����� ���ĺ� �빮��, �ҹ��ڸ� �����Ѵ�.
���� ���̵�� �г����� ���̴� 1 �̻� 10 �����̴�.
ä�ù濡�� ���� ������ �г����� �����ϴ� �� �߸� �� �Է��� �־����� �ʴ´�.
����� ��
record	result
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	["Prodo���� ���Խ��ϴ�.", "Ryan���� ���Խ��ϴ�.", "Prodo���� �������ϴ�.", "Prodo���� ���Խ��ϴ�."]
����� �� ����
����� �� #1
������ ����� ����.
'''
# def solution(record):
    
#     answer = []
#     for i in record:
#         divide = i.split(' ')
#         if answer == []:
#             answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])
#         else:
#             for j in range(len(answer)):
#                 if divide[1] == answer[j][1]:
#                     sep = answer[j][0].split(' ')
#                     if divide[0] == 'Leave':
#                         answer.append([sep[0] + ' �������ϴ�.', divide[1]])
#                         break
#                     elif divide[0] == 'Change':
#                         answer[j][0] = divide[2] + '���� ' + sep[1]
#                     else:
#                         if j != len(answer):
#                             answer[j][0] = divide[2] + '���� ' + sep[1]
#                         else:
#                             answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])
                            
                
#     res, d = zip(*answer)
#     answer = list(res)
#     print(answer)
#     return answer
# solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])


def solution(record):
    
    answer = []
    for i in record:
        divide = i.split(' ')
        if answer == []:
            answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])
        else:
            if divide[0] == 'Enter':
                for j in range(len(answer)):
                    if divide[1] == answer[j][1]:
                        sep = answer[j][0].split(' ')
                        
                        answer[j][0] = divide[2] + '���� ' + sep[1]
                answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])
            if divide[0] == 'Leave':
                for j in range(len(answer)):
                    if divide[1] == answer[j][1]:
                        sep = answer[j][0].split(' ')
                        answer.append([sep[0] + ' �������ϴ�.', divide[1]])
                        break
            else:
                for j in range(len(answer)):
                    if divide[1] == answer[j][1]:
                        sep = answer[j][0].split(' ')
                        answer[j][0] = divide[2] + '���� ' + sep[1]
                
    res, d = zip(*answer)
    answer = list(res)
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])



def solution(record):
    
    divide = record[0].split(' ')
    answer = [[divide[2] + '���� ���Խ��ϴ�.', divide[1]]]

    for i in range(1, len(record)):
        divide = record[i].split(' ')
        if divide[0] == 'Enter':
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer[j][0] = divide[2] + '���� ' + sep[1]
            answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])
            
        elif divide[0] == 'Leave':
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer.append([sep[0] + ' �������ϴ�.', divide[1]])
                    break
        else:
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer[j][0] = divide[2] + '���� ' + sep[1]
                
    res, d = zip(*answer)
    answer = list(res)
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])



def solution(record):
    name = {}   # Ű: uid1234, uid4567 ��: 
    arr = [] 
    for i in record:
        divide = i.split(' ')
        arr.append([divide[1], divide[0]])
        if divide[0] != 'Leave':
            name[divide[1]] = divide[2]
            '����' + 
            
    
    divide = record[0].split(' ')
    answer = [[divide[2] + '���� ���Խ��ϴ�.', divide[1]]]

    for i in range(1, len(record)):
        divide = record[i].split(' ')
        if divide[0] == 'Enter':
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer[j][0] = divide[2] + '���� ' + sep[1]
            answer.append([divide[2] + '���� ���Խ��ϴ�.', divide[1]])

        elif divide[0] == 'Leave':
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer.append([sep[0] + ' �������ϴ�.', divide[1]])
                    break
        else:
            for j in range(len(answer)):
                if divide[1] == answer[j][1]:
                    sep = answer[j][0].split(' ')
                    answer[j][0] = divide[2] + '���� ' + sep[1]
                
    res, d = zip(*answer)
    answer = list(res)
    return answer
solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])
            

