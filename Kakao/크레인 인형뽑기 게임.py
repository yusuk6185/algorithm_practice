# https://programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    # 줄마다 리스트를 만들어서 옮겨담기
    n = len(board)
    new_list = [[] for j in range(n)]
    answer = 0

    for i in range(n):
        for j in range(n):
            new_list[i].append(board[j][i])

    # new_list 는 각 줄의 인형 정보를 담고 있음
    picked = []
    for move in moves:
        for i in range(n):
            if new_list[move - 1][i] != 0:
                picked.append(new_list[move - 1][i])
                new_list[move-1][i] = 0
                break
                
    # picked 에서 두 개가 같으면 같이 사라짐
        if len(picked) >= 2 and picked[len(picked)-1] == picked[len(picked)-2]:
            picked.pop(-1)
            picked.pop(-1)
            answer += 1

    return answer*2

solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])