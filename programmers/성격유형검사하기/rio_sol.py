# 코드 작성 테스트
def solution(survey, choices):
    answer = ''
    board = {'R':0,'T':0,'J':0,'M':0,'A':0,'N':0,'C':0,'F':0}
    
    for idx, choice  in enumerate(choices):
        if(choice == 4):
            continue
        elif (choice<4):
            board[survey[idx][0]] += 4-choice
        else:
            board[survey[idx][1]] += choice - 4

    if(board['R']>=board['T']):
        answer += 'R'
    else:
        answer += 'T'

    if(board['C']>=board['F']):
        answer += 'C'
    else:
        answer += 'F'

    if(board['J']>=board['M']):
        answer += 'J'
    else:
        answer += 'M'

    if(board['A']>=board['N']):
        answer += 'A'
    else:
        answer += 'N'
    return answer