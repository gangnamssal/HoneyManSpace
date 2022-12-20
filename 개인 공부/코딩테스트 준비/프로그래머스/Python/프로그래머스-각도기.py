#  각 angle이 매개변수로 주어질 때
#  예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return

def solution(angle):
    if 0 < angle < 90:
        return 1
    elif angle == 90:
        return 2
    elif 90< angle < 180:
        return 3
    elif angle == 180:
        return 4
    